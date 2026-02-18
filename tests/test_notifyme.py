import pytest
from IPython.core.interactiveshell import InteractiveShell
from jupyternotifyplus.notifyme import load_ipython_extension


@pytest.fixture
def shell():
    shell = InteractiveShell.instance()
    load_ipython_extension(shell)
    return shell


def get_magics(shell):
    return shell.notifyme_magics


def test_no_notification_on_load(shell):
    magics = get_magics(shell)
    assert magics._pending_args is None
    assert "_notifyme_args" not in shell.user_ns


def test_pending_args_cleared_after_run(shell):
    shell.run_line_magic("notifyme", "-t 'Hello'")
    magics = get_magics(shell)

    assert magics._pending_args is not None

    shell.events.trigger(
        "post_run_cell", result=type("R", (), {"result": None})()
    )

    assert magics._pending_args is None


def test_variable_resolution(shell):
    shell.run_cell("a = 'Hello World'")
    shell.run_line_magic("notifyme", "success -t a")

    magics = get_magics(shell)
    args = magics._pending_args

    assert args.t == "Hello World"


def test_fstring_resolution(shell):
    shell.run_line_magic("notifyme", 'success -t f"1+1={1+1}"')

    magics = get_magics(shell)
    args = magics._pending_args

    assert args.t == "1+1=2"


def test_expression_resolution(shell):
    shell.run_line_magic("notifyme", 'success -t "3 * 7"')

    magics = get_magics(shell)
    args = magics._pending_args

    assert args.t == 21


def test_literal_fallback(shell):
    shell.run_line_magic("notifyme", 'success -t "not a valid expression!!!"')

    magics = get_magics(shell)
    args = magics._pending_args

    assert args.t == "not a valid expression!!!"
