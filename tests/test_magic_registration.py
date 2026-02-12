import os
os.environ["IPYTHON_HISTORY"] = "0"

from IPython.core.interactiveshell import InteractiveShell

def test_magic_registration():
    ip = InteractiveShell.instance()
    ip.history_manager.enabled = False  # Prevent SQLite file creation

    ip.extension_manager.load_extension("jupyternotifyplus")
    assert "notifyme" in ip.magics_manager.magics["line"]
