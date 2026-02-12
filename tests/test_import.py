import os
os.environ["IPYTHON_HISTORY"] = "0"

def test_import():
    import jupyternotifyplus
    assert hasattr(jupyternotifyplus, "load_ipython_extension")
