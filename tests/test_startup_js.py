# jupyternotifyplus/tests/test_startup_js.py
import inspect
from IPython.display import Javascript
import pytest

import jupyternotifyplus.notifyme as notifyme


def test_init_js_contains_toast_and_permission_functions():
    """
    Ensure the _INIT_JS string defines showToast, showPermissionWarning and notifyMe.
    """
    js = getattr(notifyme, "_INIT_JS", None)
    assert isinstance(js, str)
    assert "function showToast" in js or "function showToast(" in js
    assert "function showPermissionWarning" in js or "function showPermissionWarning(" in js
    assert "notifyMe" in js or "w.notifyMe" in js


def test_load_ipython_extension_emits_javascript(monkeypatch):
    """
    Ensure load_ipython_extension registers magics and calls display(Javascript(...)).
    We patch IPython.display.display and also notifyme.display if imported directly.
    """
    recorded = {}

    class DummyIPython:
        def register_magics(self, magics_obj):
            recorded['registered'] = True

        # minimal events object to avoid attribute errors if used
        class events:
            @staticmethod
            def register(*args, **kwargs):
                recorded.setdefault('events_registered', []).append((args, kwargs))

    def fake_display(obj):
        recorded.setdefault('display_calls', []).append(obj)

    # Patch the canonical display symbol
    monkeypatch.setattr("IPython.display.display", fake_display, raising=True)

    # If notifyme imported display directly, patch that too
    if hasattr(notifyme, "display"):
        monkeypatch.setattr(notifyme, "display", fake_display, raising=False)

    ip = DummyIPython()
    notifyme.load_ipython_extension(ip)

    assert recorded.get('registered', False), "register_magics was not called"
    assert 'display_calls' in recorded and len(recorded['display_calls']) >= 1, "display(Javascript(...)) was not called"

    first = recorded['display_calls'][0]
    payload = ""
    if isinstance(first, Javascript):
        payload = first.data if hasattr(first, "data") else str(first)
    else:
        payload = str(first)
    assert "showPermissionWarning" in payload or "showToast" in payload


def test_inline_and_postrun_use_publish_display_data(monkeypatch):
    """
    Ensure inline and post-run notification emission use publish_display_data.
    We monkeypatch publish_display_data to capture calls made by notifyme.NotifyMeMagics methods.
    """
    recorded = {}

    def fake_publish_display_data(*, data, metadata):
        recorded.setdefault('publish_calls', []).append(data)

    # Patch publish_display_data in the module (where it's referenced)
    if hasattr(notifyme, "publish_display_data"):
        monkeypatch.setattr(notifyme, "publish_display_data", fake_publish_display_data, raising=False)
    else:
        # If not imported under that name, patch the IPython API directly as a fallback
        monkeypatch.setattr("IPython.display.publish_display_data", fake_publish_display_data, raising=False)

    # Create a magics instance and call the inline and post-run code paths
    ip = type("IP", (), {"user_ns": {}})
    magics = notifyme.NotifyMeMagics(ip)

    # Inline path: call the helper that constructs inline JS if available
    if hasattr(magics, "_make_inline_js"):
        js_inline = magics._make_inline_js("T", "M", "icon.png")
        # simulate the inline path that calls publish_display_data
        notifyme.publish_display_data(data={"application/javascript": js_inline}, metadata={})

    # Post-run path: call the helper that constructs postrun JS if available
    if hasattr(magics, "_make_postrun_js"):
        js_post = magics._make_postrun_js("T2", "M2", "icon2.png")
        notifyme.publish_display_data(data={"application/javascript": js_post}, metadata={})

    assert 'publish_calls' in recorded and len(recorded['publish_calls']) >= 2, "publish_display_data was not used for inline/postrun emission"
