"""Test for tmuxp command line interface."""
import argparse
import io
import json
import os
import pathlib
import typing as t

import pytest

from pytest_mock import MockerFixture

import libtmux
from libtmux.common import has_lt_version
from libtmux.exc import LibTmuxException
from libtmux.session import Session
from tmuxp import cli, config, exc
from tmuxp.cli.import_config import get_teamocil_dir, get_tmuxinator_dir
from tmuxp.cli.load import (
    _load_append_windows_to_current_session,
    _load_attached,
    _reattach,
    load_plugins,
    load_workspace,
)
from tmuxp.cli.utils import (
    _validate_choices,
    get_abs_path,
    get_config_dir,
    is_pure_name,
    scan_config,
    tmuxp_echo,
)
from tmuxp.config_reader import ConfigReader
from tmuxp.workspacebuilder import WorkspaceBuilder

from .constants import FIXTURE_PATH
from .fixtures import utils as test_utils

if t.TYPE_CHECKING:
    import _pytest.capture

    from libtmux.server import Server


def test_creates_config_dir_not_exists(tmp_path: pathlib.Path) -> None:
    """cli.startup() creates config dir if not exists."""

    cli.startup(tmp_path)
    assert os.path.exists(tmp_path)


def test_in_dir_from_config_dir(tmp_path: pathlib.Path) -> None:
    """config.in_dir() finds configs config dir."""

    cli.startup(tmp_path)
    yaml_config = tmp_path / "myconfig.yaml"
    yaml_config.touch()
    json_config = tmp_path / "myconfig.json"
    json_config.touch()
    configs_found = config.in_dir(tmp_path)

    assert len(configs_found) == 2


def test_ignore_non_configs_from_current_dir(tmp_path: pathlib.Path) -> None:
    """cli.in_dir() ignore non-config from config dir."""

    cli.startup(tmp_path)

    junk_config = tmp_path / "myconfig.psd"
    junk_config.touch()
    conf = tmp_path / "watmyconfig.json"
    conf.touch()
    configs_found = config.in_dir(tmp_path)
    assert len(configs_found) == 1


def test_get_configs_cwd(
    tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """config.in_cwd() find config in shell current working directory."""

    confdir = tmp_path / "tmuxpconf2"
    confdir.mkdir()

    monkeypatch.chdir(confdir)
    config1 = open(".tmuxp.json", "w+b")
    config1.close()

    configs_found = config.in_cwd()
    assert len(configs_found) == 1
    assert ".tmuxp.json" in configs_found


@pytest.mark.parametrize(
    "path,expect",
    [
        (".", False),
        ("./", False),
        ("", False),
        (".tmuxp.yaml", False),
        ("../.tmuxp.yaml", False),
        ("../", False),
        ("/hello/world", False),
        ("~/.tmuxp/hey", False),
        ("~/work/c/tmux/", False),
        ("~/work/c/tmux/.tmuxp.yaml", False),
        ("myproject", True),
    ],
)
def test_is_pure_name(path: str, expect: bool) -> None:
    assert is_pure_name(path) == expect


"""
    scans for .tmuxp.{yaml,yml,json} in directory, returns first result
    log warning if multiple found:

    - current directory: ., ./, noarg
    - relative to cwd directory: ../, ./hello/, hello/, ./hello/
    - absolute directory: /path/to/dir, /path/to/dir/, ~/
    - no path, no ext, config_dir: projectname, tmuxp

    load file directly -

    - no directory (cwd): .tmuxp.yaml
    - relative to cwd: ../.tmuxp.yaml, ./hello/.tmuxp.yaml
    - absolute path: /path/to/file.yaml, ~/path/to/file/.tmuxp.yaml

    Any case where file is not found should return error.
"""


@pytest.fixture
def homedir(tmp_path: pathlib.Path) -> pathlib.Path:
    home = tmp_path / "home"
    home.mkdir()
    return home


@pytest.fixture
def configdir(homedir: pathlib.Path) -> pathlib.Path:
    conf = homedir / ".tmuxp"
    conf.mkdir()
    return conf


@pytest.fixture
def projectdir(homedir: pathlib.Path) -> pathlib.Path:
    proj = homedir / "work" / "project"
    proj.mkdir(parents=True)
    return proj


def test_tmuxp_configdir_env_var(
    tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("TMUXP_CONFIGDIR", str(tmp_path))

    assert get_config_dir() == str(tmp_path)


def test_tmuxp_configdir_xdg_config_dir(
    tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    tmux_dir = tmp_path / "tmuxp"
    tmux_dir.mkdir()

    assert get_config_dir() == str(tmux_dir)


def test_resolve_dot(
    tmp_path: pathlib.Path,
    homedir: pathlib.Path,
    configdir: pathlib.Path,
    projectdir: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("HOME", str(homedir))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(homedir / ".config"))

    tmuxp_conf_path = projectdir / ".tmuxp.yaml"
    tmuxp_conf_path.touch()
    user_config_name = "myconfig"
    user_config = configdir / f"{user_config_name}.yaml"
    user_config.touch()

    project_config = tmuxp_conf_path

    monkeypatch.chdir(projectdir)

    expect = str(project_config)
    assert scan_config(".") == expect
    assert scan_config("./") == expect
    assert scan_config("") == expect
    assert scan_config("../project") == expect
    assert scan_config("../project/") == expect
    assert scan_config(".tmuxp.yaml") == expect
    assert scan_config("../../.tmuxp/%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("myconfig") == str(user_config)
    assert scan_config("~/.tmuxp/myconfig.yaml") == str(user_config)

    with pytest.raises(Exception):
        scan_config(".tmuxp.json")
    with pytest.raises(Exception):
        scan_config(".tmuxp.ini")
    with pytest.raises(Exception):
        scan_config("../")
    with pytest.raises(Exception):
        scan_config("mooooooo")

    monkeypatch.chdir(homedir)

    expect = str(project_config)
    assert scan_config("work/project") == expect
    assert scan_config("work/project/") == expect
    assert scan_config("./work/project") == expect
    assert scan_config("./work/project/") == expect
    assert scan_config(".tmuxp/%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("./.tmuxp/%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("myconfig") == str(user_config)
    assert scan_config("~/.tmuxp/myconfig.yaml") == str(user_config)

    with pytest.raises(Exception):
        scan_config("")
    with pytest.raises(Exception):
        scan_config(".")
    with pytest.raises(Exception):
        scan_config(".tmuxp.yaml")
    with pytest.raises(Exception):
        scan_config("../")
    with pytest.raises(Exception):
        scan_config("mooooooo")

    monkeypatch.chdir(configdir)

    expect = str(project_config)
    assert scan_config("../work/project") == expect
    assert scan_config("../../home/work/project") == expect
    assert scan_config("../work/project/") == expect
    assert scan_config("%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("./%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("myconfig") == str(user_config)
    assert scan_config("~/.tmuxp/myconfig.yaml") == str(user_config)

    with pytest.raises(Exception):
        scan_config("")
    with pytest.raises(Exception):
        scan_config(".")
    with pytest.raises(Exception):
        scan_config(".tmuxp.yaml")
    with pytest.raises(Exception):
        scan_config("../")
    with pytest.raises(Exception):
        scan_config("mooooooo")

    monkeypatch.chdir(tmp_path)

    expect = str(project_config)
    assert scan_config("home/work/project") == expect
    assert scan_config("./home/work/project/") == expect
    assert scan_config("home/.tmuxp/%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("./home/.tmuxp/%s.yaml" % user_config_name) == str(user_config)
    assert scan_config("myconfig") == str(user_config)
    assert scan_config("~/.tmuxp/myconfig.yaml") == str(user_config)

    with pytest.raises(Exception):
        scan_config("")
    with pytest.raises(Exception):
        scan_config(".")
    with pytest.raises(Exception):
        scan_config(".tmuxp.yaml")
    with pytest.raises(Exception):
        scan_config("../")
    with pytest.raises(Exception):
        scan_config("mooooooo")


def test_scan_config_arg(
    homedir: pathlib.Path,
    configdir: pathlib.Path,
    projectdir: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str)

    def config_cmd(config_file: str) -> None:
        tmuxp_echo(scan_config(config_file, config_dir=configdir))

    monkeypatch.setenv("HOME", str(homedir))
    tmuxp_config_path = projectdir / ".tmuxp.yaml"
    tmuxp_config_path.touch()
    user_config_name = "myconfig"
    user_config = configdir / f"{user_config_name}.yaml"
    user_config.touch()

    project_config = projectdir / ".tmuxp.yaml"

    def check_cmd(config_arg) -> "_pytest.capture.CaptureResult":
        args = parser.parse_args([config_arg])
        config_cmd(config_file=args.config_file)
        return capsys.readouterr()

    monkeypatch.chdir(projectdir)
    expect = str(project_config)
    assert expect in check_cmd(".").out
    assert expect in check_cmd("./").out
    assert expect in check_cmd("").out
    assert expect in check_cmd("../project").out
    assert expect in check_cmd("../project/").out
    assert expect in check_cmd(".tmuxp.yaml").out
    assert str(user_config) in check_cmd("../../.tmuxp/%s.yaml" % user_config_name).out
    assert user_config.stem in check_cmd("myconfig").out
    assert str(user_config) in check_cmd("~/.tmuxp/myconfig.yaml").out

    with pytest.raises(FileNotFoundError, match="file not found"):
        assert "file not found" in check_cmd(".tmuxp.json").err
    with pytest.raises(FileNotFoundError, match="file not found"):
        assert "file not found" in check_cmd(".tmuxp.ini").err
    with pytest.raises(FileNotFoundError, match="No tmuxp files found"):
        assert "No tmuxp files found" in check_cmd("../").err
    with pytest.raises(FileNotFoundError, match="config not found in config dir"):
        assert "config not found in config dir" in check_cmd("moo").err


def test_load_workspace(server: "Server", monkeypatch: pytest.MonkeyPatch) -> None:
    # this is an implementation test. Since this testsuite may be ran within
    # a tmux session by the developer himself, delete the TMUX variable
    # temporarily.
    monkeypatch.delenv("TMUX", raising=False)
    session_file = FIXTURE_PATH / "workspacebuilder" / "two_pane.yaml"

    # open it detached
    session = load_workspace(
        session_file, socket_name=server.socket_name, detached=True
    )

    assert isinstance(session, Session)
    assert session.name == "sampleconfig"


def test_load_workspace_named_session(
    server: "Server", monkeypatch: pytest.MonkeyPatch
) -> None:
    # this is an implementation test. Since this testsuite may be ran within
    # a tmux session by the developer himself, delete the TMUX variable
    # temporarily.
    monkeypatch.delenv("TMUX", raising=False)
    session_file = FIXTURE_PATH / "workspacebuilder" / "two_pane.yaml"

    # open it detached
    session = load_workspace(
        session_file,
        socket_name=server.socket_name,
        new_session_name="tmuxp-new",
        detached=True,
    )

    assert isinstance(session, Session)
    assert session.name == "tmuxp-new"


@pytest.mark.skipif(
    has_lt_version("2.1"), reason="exact session name matches only tmux >= 2.1"
)
def test_load_workspace_name_match_regression_252(
    tmp_path: pathlib.Path, server: "Server", monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("TMUX", raising=False)
    session_file = FIXTURE_PATH / "workspacebuilder" / "two_pane.yaml"

    # open it detached
    session = load_workspace(
        session_file, socket_name=server.socket_name, detached=True
    )

    assert isinstance(session, Session)
    assert session.name == "sampleconfig"

    projfile = tmp_path / "simple.yaml"

    projfile.write_text(
        """
session_name: sampleconfi
start_directory: './'
windows:
- panes:
    - echo 'hey'""",
        encoding="utf-8",
    )

    # open it detached
    session = load_workspace(
        str(projfile), socket_name=server.socket_name, detached=True
    )
    assert session is not None
    assert session.name == "sampleconfi"


def test_load_symlinked_workspace(
    server: "Server", tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # this is an implementation test. Since this testsuite may be ran within
    # a tmux session by the developer himself, delete the TMUX variable
    # temporarily.
    monkeypatch.delenv("TMUX", raising=False)

    realtemp = tmp_path / "myrealtemp"
    realtemp.mkdir()
    linktemp = tmp_path / "symlinktemp"
    linktemp.symlink_to(realtemp)
    projfile = linktemp / "simple.yaml"

    projfile.write_text(
        """
session_name: samplesimple
start_directory: './'
windows:
- panes:
    - echo 'hey'""",
        encoding="utf-8",
    )

    # open it detached
    session = load_workspace(
        str(projfile), socket_name=server.socket_name, detached=True
    )
    assert session is not None
    assert session.attached_window is not None
    pane = session.attached_window.attached_pane

    assert isinstance(session, Session)
    assert session.name == "samplesimple"

    assert pane is not None
    assert pane.current_path == str(realtemp)


def test_regression_00132_session_name_with_dots(
    tmp_path: pathlib.Path,
    server: "Server",
    session: Session,
    capsys: pytest.CaptureFixture,
) -> None:
    yaml_config = FIXTURE_PATH / "workspacebuilder" / "regression_00132_dots.yaml"
    cli_args = [str(yaml_config)]
    with pytest.raises(libtmux.exc.BadSessionName):
        cli.cli(["load", *cli_args])


@pytest.mark.parametrize(
    "cli_args", [["load", ".", "-d"], ["load", ".tmuxp.yaml", "-d"]]
)
def test_load_zsh_autotitle_warning(
    cli_args: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
    server: "Server",
) -> None:
    # create dummy tmuxp yaml so we don't get yelled at
    yaml_config = tmp_path / ".tmuxp.yaml"
    yaml_config.write_text(
        """
    session_name: test
    windows:
    - window_name: test
      panes:
      -
    """,
        encoding="utf-8",
    )
    oh_my_zsh_path = tmp_path / ".oh-my-zsh"
    oh_my_zsh_path.mkdir()
    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.chdir(tmp_path)

    monkeypatch.delenv("DISABLE_AUTO_TITLE", raising=False)
    monkeypatch.setenv("SHELL", "zsh")

    # Use tmux server (socket name) used in the test
    assert server.socket_name is not None
    cli_args = cli_args + ["-L", server.socket_name]

    cli.cli(cli_args)
    result = capsys.readouterr()
    assert "Please set" in result.out

    monkeypatch.setenv("DISABLE_AUTO_TITLE", "false")
    cli.cli(cli_args)
    result = capsys.readouterr()
    assert "Please set" in result.out

    monkeypatch.setenv("DISABLE_AUTO_TITLE", "true")
    cli.cli(cli_args)
    result = capsys.readouterr()
    assert "Please set" not in result.out

    monkeypatch.delenv("DISABLE_AUTO_TITLE", raising=False)
    monkeypatch.setenv("SHELL", "sh")
    cli.cli(cli_args)
    result = capsys.readouterr()
    assert "Please set" not in result.out


@pytest.mark.parametrize(
    "cli_args",
    [
        (["load", ".", "--log-file", "log.txt", "-d"]),
    ],
)
def test_load_log_file(
    cli_args: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    # create dummy tmuxp yaml that breaks to prevent actually loading tmux
    tmuxp_config_path = tmp_path / ".tmuxp.yaml"
    tmuxp_config_path.write_text(
        """
session_name: hello
  -
        """,
        encoding="utf-8",
    )
    oh_my_zsh_path = tmp_path / ".oh-my-zsh"
    oh_my_zsh_path.mkdir()
    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.chdir(tmp_path)

    try:
        cli.cli(cli_args)
    except Exception:
        pass
    result = capsys.readouterr()
    log_file_path = tmp_path / "log.txt"
    assert "Loading" in log_file_path.open().read()
    assert result.out is not None


@pytest.mark.parametrize("cli_cmd", [["shell"], ["shell", "--pdb"]])
@pytest.mark.parametrize(
    "cli_args,inputs,env,expected_output",
    [
        (
            ["-L{SOCKET_NAME}", "-c", "print(str(server.socket_name))"],
            [],
            {},
            "{SERVER_SOCKET_NAME}",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "{SESSION_NAME}",
                "-c",
                "print(session.name)",
            ],
            [],
            {},
            "{SESSION_NAME}",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "{SESSION_NAME}",
                "{WINDOW_NAME}",
                "-c",
                "print(server.has_session(session.name))",
            ],
            [],
            {},
            "True",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "{SESSION_NAME}",
                "{WINDOW_NAME}",
                "-c",
                "print(window.name)",
            ],
            [],
            {},
            "{WINDOW_NAME}",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "{SESSION_NAME}",
                "{WINDOW_NAME}",
                "-c",
                "print(pane.id)",
            ],
            [],
            {},
            "{PANE_ID}",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "-c",
                "print(pane.id)",
            ],
            [],
            {"TMUX_PANE": "{PANE_ID}"},
            "{PANE_ID}",
        ),
    ],
)
def test_shell(
    cli_cmd: t.List[str],
    cli_args: t.List[str],
    inputs: t.List[t.Any],
    expected_output: str,
    env: t.Dict[str, str],
    server: "Server",
    session: Session,
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    window_name = "my_window"
    window = session.new_window(window_name=window_name)
    window.split_window()

    assert window.attached_pane is not None

    template_ctx = dict(
        SOCKET_NAME=server.socket_name,
        SESSION_NAME=session.name,
        WINDOW_NAME=window_name,
        PANE_ID=window.attached_pane.id,
        SERVER_SOCKET_NAME=server.socket_name,
    )

    cli_args = cli_cmd + [cli_arg.format(**template_ctx) for cli_arg in cli_args]

    for k, v in env.items():
        monkeypatch.setenv(k, v.format(**template_ctx))

    monkeypatch.chdir(tmp_path)

    cli.cli(cli_args)
    result = capsys.readouterr()
    assert expected_output.format(**template_ctx) in result.out


@pytest.mark.parametrize(
    "cli_cmd",
    [
        ["shell"],
        ["shell", "--pdb"],
    ],
)
@pytest.mark.parametrize(
    "cli_args,inputs,env,template_ctx,exception,message",
    [
        (
            ["-LDoesNotExist", "-c", "print(str(server.socket_name))"],
            [],
            {},
            {},
            LibTmuxException,
            r".*DoesNotExist.*",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "nonexistant_session",
                "-c",
                "print(str(server.socket_name))",
            ],
            [],
            {},
            {"session_name": "nonexistant_session"},
            exc.TmuxpException,
            "Session not found: nonexistant_session",
        ),
        (
            [
                "-L{SOCKET_NAME}",
                "{SESSION_NAME}",
                "nonexistant_window",
                "-c",
                "print(str(server.socket_name))",
            ],
            [],
            {},
            {"window_name": "nonexistant_window"},
            exc.TmuxpException,
            "Window not found: {WINDOW_NAME}",
        ),
    ],
)
def test_shell_target_missing(
    cli_cmd: t.List[str],
    cli_args: t.List[str],
    inputs: t.List[t.Any],
    env: t.Dict[t.Any, t.Any],
    template_ctx: t.Dict[str, str],
    exception: t.Union[t.Type[exc.TmuxpException], t.Type[LibTmuxException]],
    message: str,
    socket_name: str,
    server: "Server",
    session: Session,
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    window_name = "my_window"
    window = session.new_window(window_name=window_name)
    window.split_window()

    assert server.socket_name is not None
    assert session.name is not None

    template_ctx.update(
        dict(
            SOCKET_NAME=server.socket_name,
            SESSION_NAME=session.name,
            WINDOW_NAME=template_ctx.get("window_name", window_name),
        )
    )
    cli_args = cli_cmd + [cli_arg.format(**template_ctx) for cli_arg in cli_args]

    for k, v in env.items():
        monkeypatch.setenv(k, v.format(**template_ctx))

    monkeypatch.chdir(tmp_path)

    if exception is not None:
        with pytest.raises(exception, match=message.format(**template_ctx)):
            cli.cli(cli_args)
    else:
        cli.cli(cli_args)
        result = capsys.readouterr()
        assert message.format(**template_ctx) in result.out


@pytest.mark.parametrize(
    "cli_cmd",
    [
        # ['shell'],
        # ['shell', '--pdb'),
        ["shell", "--code"],
        # ['shell', '--bpython'],
        # ['shell', '--ptipython'],
        # ['shell', '--ptpython'],
        # ['shell', '--ipython'],
    ],
)
@pytest.mark.parametrize(
    "cli_args,inputs,env,message",
    [
        (
            [
                "-L{SOCKET_NAME}",
            ],
            [],
            {},
            "(InteractiveConsole)",
        ),
        (
            [
                "-L{SOCKET_NAME}",
            ],
            [],
            {"PANE_ID": "{PANE_ID}"},
            "(InteractiveConsole)",
        ),
    ],
)
def test_shell_interactive(
    cli_cmd: t.List[str],
    cli_args: t.List[str],
    inputs: t.List[t.Any],
    env: t.Dict[str, str],
    message: str,
    server: "Server",
    session: Session,
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    window_name = "my_window"
    window = session.new_window(window_name=window_name)
    window.split_window()

    assert window.attached_pane is not None

    template_ctx = dict(
        SOCKET_NAME=server.socket_name,
        SESSION_NAME=session.name,
        WINDOW_NAME=window_name,
        PANE_ID=window.attached_pane.id,
        SERVER_SOCKET_NAME=server.socket_name,
    )

    cli_args = cli_cmd + [cli_arg.format(**template_ctx) for cli_arg in cli_args]

    for k, v in env.items():
        monkeypatch.setenv(k, v.format(**template_ctx))

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.stdin", io.StringIO("exit()\r"))
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass
    result = capsys.readouterr()
    assert message.format(**template_ctx) in result.err


@pytest.mark.parametrize(
    "cli_args",
    [
        (["convert", "."]),
        (["convert", ".tmuxp.yaml"]),
        (["convert", ".tmuxp.yaml", "-y"]),
        (["convert", ".tmuxp.yml"]),
        (["convert", ".tmuxp.yml", "-y"]),
    ],
)
def test_convert(
    cli_args: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # create dummy tmuxp yaml so we don't get yelled at
    filename = cli_args[1]
    if filename == ".":
        filename = ".tmuxp.yaml"
    file_ext = filename.rsplit(".", 1)[-1]
    assert file_ext in ["yaml", "yml"], file_ext
    config_file_path = tmp_path / filename
    config_file_path.write_text("\nsession_name: hello\n", encoding="utf-8")
    oh_my_zsh_path = tmp_path / ".oh-my-zsh"
    oh_my_zsh_path.mkdir()
    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.chdir(tmp_path)

    # If autoconfirm (-y) no need to prompt y
    input_args = "y\ny\n" if "-y" not in cli_args else ""

    monkeypatch.setattr("sys.stdin", io.StringIO(input_args))
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass
    tmuxp_json = tmp_path / ".tmuxp.json"
    assert tmuxp_json.exists()
    assert tmuxp_json.open().read() == json.dumps({"session_name": "hello"}, indent=2)


@pytest.mark.parametrize(
    "cli_args",
    [
        (["convert", "."]),
        (["convert", ".tmuxp.json"]),
        (["convert", ".tmuxp.json", "-y"]),
    ],
)
def test_convert_json(
    cli_args: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # create dummy tmuxp yaml so we don't get yelled at
    json_config = tmp_path / ".tmuxp.json"
    json_config.write_text('{"session_name": "hello"}', encoding="utf-8")
    oh_my_zsh_path = tmp_path / ".oh-my-zsh"
    oh_my_zsh_path.mkdir()
    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.chdir(tmp_path)

    # If autoconfirm (-y) no need to prompt y
    input_args = "y\ny\n" if "-y" not in cli_args else ""

    monkeypatch.setattr("sys.stdin", io.StringIO(input_args))
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass

    tmuxp_yaml = tmp_path / ".tmuxp.yaml"
    assert tmuxp_yaml.exists()
    assert tmuxp_yaml.open().read() == "session_name: hello\n"


@pytest.mark.parametrize("cli_args", [(["import"])])
def test_import(
    cli_args: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    cli.cli(cli_args)
    result = capsys.readouterr()
    assert "tmuxinator" in result.out
    assert "teamocil" in result.out


@pytest.mark.parametrize(
    "cli_args",
    [
        (["--help"]),
        (["-h"]),
    ],
)
def test_help(
    cli_args: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass
    result = capsys.readouterr()

    assert "usage: tmuxp [-h] [--version] [--log-level LOG_LEVEL]" in result.out


@pytest.mark.parametrize(
    "cli_args,inputs",
    [
        (
            ["import", "teamocil", "./.teamocil/config.yaml"],
            ["\n", "y\n", "./la.yaml\n", "y\n"],
        ),
        (
            ["import", "teamocil", "./.teamocil/config.yaml"],
            ["\n", "y\n", "./exists.yaml\n", "./la.yaml\n", "y\n"],
        ),
        (
            ["import", "teamocil", "config"],
            ["\n", "y\n", "./exists.yaml\n", "./la.yaml\n", "y\n"],
        ),
    ],
)
def test_import_teamocil(
    cli_args: t.List[str],
    inputs: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    teamocil_config = test_utils.read_config_file("config_teamocil/test4.yaml")

    teamocil_path = tmp_path / ".teamocil"
    teamocil_path.mkdir()

    teamocil_config_path = teamocil_path / "config.yaml"
    teamocil_config_path.write_text(teamocil_config, encoding="utf-8")

    exists_yaml = tmp_path / "exists.yaml"
    exists_yaml.touch()

    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.stdin", io.StringIO("".join(inputs)))

    try:
        cli.cli(cli_args)
    except SystemExit:
        pass

    new_config_yaml = tmp_path / "la.yaml"
    assert new_config_yaml.exists()


@pytest.mark.parametrize(
    "cli_args,inputs",
    [
        (
            ["import", "tmuxinator", "./.tmuxinator/config.yaml"],
            ["\n", "y\n", "./la.yaml\n", "y\n"],
        ),
        (
            ["import", "tmuxinator", "./.tmuxinator/config.yaml"],
            ["\n", "y\n", "./exists.yaml\n", "./la.yaml\n", "y\n"],
        ),
        (
            ["import", "tmuxinator", "config"],
            ["\n", "y\n", "./exists.yaml\n", "./la.yaml\n", "y\n"],
        ),
    ],
)
def test_import_tmuxinator(
    cli_args: t.List[str],
    inputs: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    tmuxinator_config = test_utils.read_config_file("config_tmuxinator/test3.yaml")

    tmuxinator_path = tmp_path / ".tmuxinator"
    tmuxinator_path.mkdir()

    tmuxinator_config_path = tmuxinator_path / "config.yaml"
    tmuxinator_config_path.write_text(tmuxinator_config, encoding="utf-8")

    exists_yaml = tmp_path / "exists.yaml"
    exists_yaml.touch()

    monkeypatch.setenv("HOME", str(tmp_path))

    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr("sys.stdin", io.StringIO("".join(inputs)))
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass

    new_config_yaml = tmp_path / "la.yaml"
    assert new_config_yaml.exists()


@pytest.mark.parametrize(
    "cli_args,inputs",
    [
        (["freeze", "myfrozensession"], ["y\n", "./la.yaml\n", "y\n"]),
        (  # Exists
            ["freeze", "myfrozensession"],
            ["y\n", "./exists.yaml\n", "./la.yaml\n", "y\n"],
        ),
        (  # Imply current session if not entered
            ["freeze"],
            ["y\n", "./la.yaml\n", "y\n"],
        ),
        (["freeze"], ["y\n", "./exists.yaml\n", "./la.yaml\n", "y\n"]),  # Exists
    ],
)
def test_freeze(
    server: "Server",
    cli_args: t.List[str],
    inputs: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    exists_yaml = tmp_path / "exists.yaml"
    exists_yaml.touch()

    server.new_session(session_name="myfirstsession")
    server.new_session(session_name="myfrozensession")

    # Assign an active pane to the session
    second_session = server.list_sessions()[1]
    first_pane_on_second_session_id = second_session.list_windows()[0].list_panes()[0][
        "pane_id"
    ]
    monkeypatch.setenv("TMUX_PANE", first_pane_on_second_session_id)

    monkeypatch.chdir(tmp_path)
    # Use tmux server (socket name) used in the test
    assert server.socket_name is not None
    cli_args = cli_args + ["-L", server.socket_name]

    monkeypatch.setattr("sys.stdin", io.StringIO("".join(inputs)))
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass

    yaml_config_path = tmp_path / "la.yaml"
    assert yaml_config_path.exists()

    yaml_config = yaml_config_path.open().read()
    frozen_config = ConfigReader._load(format="yaml", content=yaml_config)

    assert frozen_config["session_name"] == "myfrozensession"


@pytest.mark.parametrize(
    "cli_args,inputs",
    [
        (  # Overwrite
            ["freeze", "mysession", "--force"],
            ["\n", "\n", "y\n", "./exists.yaml\n", "y\n"],
        ),
        (  # Imply current session if not entered
            ["freeze", "--force"],
            ["\n", "\n", "y\n", "./exists.yaml\n", "y\n"],
        ),
    ],
)
def test_freeze_overwrite(
    server: "Server",
    cli_args: t.List[str],
    inputs: t.List[str],
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    exists_yaml = tmp_path / "exists.yaml"
    exists_yaml.touch()

    server.new_session(session_name="mysession")

    monkeypatch.chdir(tmp_path)
    # Use tmux server (socket name) used in the test
    assert server.socket_name is not None
    cli_args = cli_args + ["-L", server.socket_name]

    monkeypatch.setattr("sys.stdin", io.StringIO("".join(inputs)))
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass

    yaml_config_path = tmp_path / "exists.yaml"
    assert yaml_config_path.exists()


def test_get_abs_path(tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
    expect = str(tmp_path)
    monkeypatch.chdir(tmp_path)
    get_abs_path("../") == os.path.dirname(expect)
    get_abs_path(".") == expect
    get_abs_path("./") == expect
    get_abs_path(expect) == expect


def test_get_tmuxinator_dir(monkeypatch: pytest.MonkeyPatch) -> None:
    assert get_tmuxinator_dir() == os.path.expanduser("~/.tmuxinator/")

    monkeypatch.setenv("HOME", "/moo")
    assert get_tmuxinator_dir() == "/moo/.tmuxinator/"
    assert get_tmuxinator_dir() == os.path.expanduser("~/.tmuxinator/")


def test_get_teamocil_dir(monkeypatch: pytest.MonkeyPatch) -> None:
    assert get_teamocil_dir() == os.path.expanduser("~/.teamocil/")

    monkeypatch.setenv("HOME", "/moo")
    assert get_teamocil_dir() == "/moo/.teamocil/"
    assert get_teamocil_dir() == os.path.expanduser("~/.teamocil/")


def test_validate_choices() -> None:
    validate = _validate_choices(["choice1", "choice2"])

    assert validate("choice1")
    assert validate("choice2")

    with pytest.raises(ValueError):
        assert validate("choice3")


def test_pass_config_dir_ClickPath(
    tmp_path: pathlib.Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:

    configdir = tmp_path / "myconfigdir"
    configdir.mkdir()
    user_config_name = "myconfig"
    user_config = configdir / f"{user_config_name}.yaml"
    user_config.touch()

    expect = str(user_config)

    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str)

    def config_cmd(config_file: str) -> None:
        tmuxp_echo(scan_config(config_file, config_dir=configdir))

    def check_cmd(config_arg) -> "_pytest.capture.CaptureResult":
        args = parser.parse_args([config_arg])
        config_cmd(config_file=args.config_file)
        return capsys.readouterr()

    monkeypatch.chdir(configdir)

    assert expect in check_cmd("myconfig").out
    assert expect in check_cmd("myconfig.yaml").out
    assert expect in check_cmd("./myconfig.yaml").out
    assert str(user_config) in check_cmd(str(configdir / "myconfig.yaml")).out

    with pytest.raises(FileNotFoundError):
        assert "FileNotFoundError" in check_cmd(".tmuxp.json").out


def test_ls_cli(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: pathlib.Path,
    capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / ".config"))

    filenames = [
        ".git/",
        ".gitignore/",
        "session_1.yaml",
        "session_2.yaml",
        "session_3.json",
        "session_4.txt",
    ]

    # should ignore:
    # - directories should be ignored
    # - extensions not covered in VALID_CONFIG_DIR_FILE_EXTENSIONS
    ignored_filenames = [".git/", ".gitignore/", "session_4.txt"]
    stems = [os.path.splitext(f)[0] for f in filenames if f not in ignored_filenames]

    for filename in filenames:
        location = tmp_path / f".tmuxp/{filename}"
        if filename.endswith("/"):
            location.mkdir(parents=True)
        else:
            location.touch()

    try:
        cli.cli(["ls"])
    except SystemExit:
        pass
    cli_output = capsys.readouterr().out

    assert cli_output == "\n".join(stems) + "\n"


def test_load_plugins(monkeypatch_plugin_test_packages: None) -> None:
    from tmuxp_test_plugin_bwb.plugin import PluginBeforeWorkspaceBuilder

    plugins_config = test_utils.read_config_file("workspacebuilder/plugin_bwb.yaml")

    sconfig = ConfigReader._load(format="yaml", content=plugins_config)
    sconfig = config.expand(sconfig)

    plugins = load_plugins(sconfig)

    assert len(plugins) == 1

    test_plugin_class_types = [
        PluginBeforeWorkspaceBuilder().__class__,
    ]
    for plugin in plugins:
        assert plugin.__class__ in test_plugin_class_types


@pytest.mark.skip("Not sure how to clean up the tmux session this makes")
@pytest.mark.parametrize(
    "cli_args,inputs",
    [
        (
            ["load", "tests/fixtures/workspacebuilder/plugin_versions_fail.yaml"],
            ["y\n"],
        )
    ],
)
def test_load_plugins_version_fail_skip(
    monkeypatch_plugin_test_packages, cli_args, inputs, capsys: pytest.CaptureFixture
) -> None:
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass
    result = capsys.readouterr()

    assert "[Loading]" in result.out


@pytest.mark.parametrize(
    "cli_args,inputs",
    [
        (
            ["load", "tests/fixtures/workspacebuilder/plugin_versions_fail.yaml"],
            ["n\n"],
        )
    ],
)
def test_load_plugins_version_fail_no_skip(
    monkeypatch_plugin_test_packages: None,
    cli_args: t.List[str],
    inputs: t.List[str],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("".join(inputs)))

    try:
        cli.cli(cli_args)
    except SystemExit:
        pass
    result = capsys.readouterr()

    assert "[Not Skipping]" in result.out


@pytest.mark.parametrize(
    "cli_args", [(["load", "tests/fixtures/workspacebuilder/plugin_missing_fail.yaml"])]
)
def test_load_plugins_plugin_missing(
    monkeypatch_plugin_test_packages: None,
    cli_args: t.List[str],
    capsys: pytest.CaptureFixture,
) -> None:
    try:
        cli.cli(cli_args)
    except SystemExit:
        pass
    result = capsys.readouterr()

    assert "[Plugin Error]" in result.out


def test_plugin_system_before_script(
    monkeypatch_plugin_test_packages: None,
    server: "Server",
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # this is an implementation test. Since this testsuite may be ran within
    # a tmux session by the developer himself, delete the TMUX variable
    # temporarily.
    monkeypatch.delenv("TMUX", raising=False)
    session_file = FIXTURE_PATH / "workspacebuilder" / "plugin_bs.yaml"

    # open it detached
    session = load_workspace(
        session_file, socket_name=server.socket_name, detached=True
    )

    assert isinstance(session, libtmux.Session)
    assert session.name == "plugin_test_bs"


def test_reattach_plugins(
    monkeypatch_plugin_test_packages: None, server: "Server"
) -> None:
    config_plugins = test_utils.read_config_file("workspacebuilder/plugin_r.yaml")

    sconfig = ConfigReader._load(format="yaml", content=config_plugins)
    sconfig = config.expand(sconfig)

    # open it detached
    builder = WorkspaceBuilder(
        sconf=sconfig, plugins=load_plugins(sconfig), server=server
    )
    builder.build()

    try:
        _reattach(builder)
    except libtmux.exc.LibTmuxException:
        pass

    proc = builder.session.cmd("display-message", "-p", "'#S'")

    assert proc.stdout[0] == "'plugin_test_r'"


def test_load_attached(
    server: "Server", monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture
) -> None:
    # Load a session and attach from outside tmux
    monkeypatch.delenv("TMUX", raising=False)

    attach_session_mock = mocker.patch("libtmux.session.Session.attach_session")
    attach_session_mock.return_value.stderr = None

    yaml_config = test_utils.read_config_file("workspacebuilder/two_pane.yaml")
    sconfig = ConfigReader._load(format="yaml", content=yaml_config)

    builder = WorkspaceBuilder(sconf=sconfig, server=server)

    _load_attached(builder, False)

    assert attach_session_mock.call_count == 1


def test_load_attached_detached(
    server: "Server", monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture
) -> None:
    # Load a session but don't attach
    monkeypatch.delenv("TMUX", raising=False)

    attach_session_mock = mocker.patch("libtmux.session.Session.attach_session")
    attach_session_mock.return_value.stderr = None

    yaml_config = test_utils.read_config_file("workspacebuilder/two_pane.yaml")
    sconfig = ConfigReader._load(format="yaml", content=yaml_config)

    builder = WorkspaceBuilder(sconf=sconfig, server=server)

    _load_attached(builder, True)

    assert attach_session_mock.call_count == 0


def test_load_attached_within_tmux(
    server: "Server", monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture
) -> None:
    # Load a session and attach from within tmux
    monkeypatch.setenv("TMUX", "/tmp/tmux-1234/default,123,0")

    switch_client_mock = mocker.patch("libtmux.session.Session.switch_client")
    switch_client_mock.return_value.stderr = None

    yaml_config = test_utils.read_config_file("workspacebuilder/two_pane.yaml")
    sconfig = ConfigReader._load(format="yaml", content=yaml_config)

    builder = WorkspaceBuilder(sconf=sconfig, server=server)

    _load_attached(builder, False)

    assert switch_client_mock.call_count == 1


def test_load_attached_within_tmux_detached(
    server: "Server", monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture
) -> None:
    # Load a session and attach from within tmux
    monkeypatch.setenv("TMUX", "/tmp/tmux-1234/default,123,0")

    switch_client_mock = mocker.patch("libtmux.session.Session.switch_client")
    switch_client_mock.return_value.stderr = None

    yaml_config = test_utils.read_config_file("workspacebuilder/two_pane.yaml")
    sconfig = ConfigReader._load(format="yaml", content=yaml_config)

    builder = WorkspaceBuilder(sconf=sconfig, server=server)

    _load_attached(builder, True)

    assert switch_client_mock.call_count == 1


def test_load_append_windows_to_current_session(
    server: "Server", monkeypatch: pytest.MonkeyPatch
) -> None:
    yaml_config = test_utils.read_config_file("workspacebuilder/two_pane.yaml")
    sconfig = ConfigReader._load(format="yaml", content=yaml_config)

    builder = WorkspaceBuilder(sconf=sconfig, server=server)
    builder.build()

    assert len(server.list_sessions()) == 1
    assert len(server._list_windows()) == 3

    # Assign an active pane to the session
    monkeypatch.setenv("TMUX_PANE", server._list_panes()[0]["pane_id"])

    builder = WorkspaceBuilder(sconf=sconfig, server=server)
    _load_append_windows_to_current_session(builder)

    assert len(server.list_sessions()) == 1
    assert len(server._list_windows()) == 6


def test_debug_info_cli(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: pathlib.Path,
    capsys: pytest.CaptureFixture,
) -> None:
    monkeypatch.setenv("SHELL", "/bin/bash")

    cli.cli(["debug-info"])
    cli_output = capsys.readouterr().out
    assert "environment" in cli_output
    assert "python version" in cli_output
    assert "system PATH" in cli_output
    assert "tmux version" in cli_output
    assert "libtmux version" in cli_output
    assert "tmuxp version" in cli_output
    assert "tmux path" in cli_output
    assert "tmuxp path" in cli_output
    assert "shell" in cli_output
    assert "tmux session" in cli_output
    assert "tmux windows" in cli_output
    assert "tmux panes" in cli_output
    assert "tmux global options" in cli_output
    assert "tmux window options" in cli_output
