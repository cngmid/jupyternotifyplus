import pytest
from IPython.core.interactiveshell import InteractiveShell
from jupyternotifyplus.notifyme import load_ipython_extension


@pytest.fixture
def shell():
    shell = InteractiveShell.instance()
    load_ipython_extension(shell)
    return shell


def test_no_notification_on_load(shell):
    """
    Ensures that simply loading the extension does not schedule
    notifications.
    """
    assert getattr(
        shell.magics_manager.magics['line'], 'notifyme'
    )._pending_args is None


def test_pending_args_cleared_after_run(shell):
    """
    Ensures that pending args are cleared after post_run_cell executes.
    """
    shell.run_line_magic("notifyme", "-t 'Hello'")
    magics = shell.magics_manager.magics['line']['notifyme']

    # Pending args should be set
    assert magics._pending_args is not None

    # Simulate cell execution
    shell.events.trigger(
        "post_run_cell", result=type("R", (), {"result": None})()
    )

    # Pending args should now be cleared
    assert magics._pending_args is None


def test_variable_resolution(shell):
    shell.run_cell("a = 'Hello World'")
    shell.run_line_magic("notifyme", "success -t a")

    args = shell.user_ns["_notifyme_args"]
    assert args.t == "Hello World"


def test_fstring_resolution(shell):
    shell.run_line_magic("notifyme", 'success -t f"1+1={1+1}"')

    args = shell.user_ns["_notifyme_args"]
    assert args.t == "1+1=2"


def test_expression_resolution(shell):
    shell.run_line_magic("notifyme", 'success -t "3 * 7"')

    args = shell.user_ns["_notifyme_args"]
    assert args.t == 21


def test_literal_fallback(shell):
    # Invalid expression should fall back to literal string
    shell.run_line_magic("notifyme", 'success -t "not a valid expression!!!"')

    args = shell.user_ns["_notifyme_args"]
    assert args.t == "not a valid expression!!!"
