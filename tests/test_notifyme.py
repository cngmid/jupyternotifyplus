import pytest
from IPython.core.interactiveshell import InteractiveShell
from jupyternotifyplus.notifyme import load_ipython_extension


@pytest.fixture
def shell():
    shell = InteractiveShell.instance()
    load_ipython_extension(shell)
    return shell


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
