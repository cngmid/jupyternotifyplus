import argparse
import shlex
from datetime import datetime

from IPython.core.magic import Magics, magics_class, line_magic
from IPython.display import publish_display_data
from IPython.display import Javascript, display

# Default icon
DEFAULT_ICON = "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/2139.png"

# JavaScript injected once per kernel session
# IMPORTANT: This guard prevents notifications during notebook restore.
_INIT_JS = r"""
(function() {
    var w = window;
    while (w !== w.parent) {
        w = w.parent;
    }

    function ensureToastContainer() {
        var existing = w.document.getElementById("jnp-toast-container");
        if (existing) return existing;

        var container = w.document.createElement("div");
        container.id = "jnp-toast-container";
        container.style.position = "fixed";
        container.style.bottom = "20px";
        container.style.right = "20px";
        container.style.zIndex = 9999;
        container.style.display = "flex";
        container.style.flexDirection = "column";
        container.style.gap = "8px";
        w.document.body.appendChild(container);
        return container;
    }

    function showToast(title, body) {
        var container = ensureToastContainer();
        var toast = w.document.createElement("div");
        toast.style.background = "rgba(40, 40, 40, 0.95)";
        toast.style.color = "white";
        toast.style.padding = "10px 14px";
        toast.style.borderRadius = "4px";
        toast.style.boxShadow = "0 2px 6px rgba(0,0,0,0.4)";
        toast.style.fontFamily = "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif";
        toast.style.fontSize = "13px";
        toast.style.maxWidth = "320px";

        var titleEl = w.document.createElement("div");
        titleEl.textContent = title || "Notification";
        titleEl.style.fontWeight = "600";
        titleEl.style.marginBottom = body ? "2px" : "0";

        var bodyEl = w.document.createElement("div");
        bodyEl.textContent = body || "";
        bodyEl.style.fontWeight = "400";

        toast.appendChild(titleEl);
        if (body) {
            toast.appendChild(bodyEl);
        }

        container.appendChild(toast);

        setTimeout(function() {
            toast.style.transition = "opacity 0.4s ease, transform 0.4s ease";
            toast.style.opacity = "0";
            toast.style.transform = "translateY(5px)";
            setTimeout(function() {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 400);
        }, 3500);
    }

    function showPermissionWarning() {
        var existing = w.document.getElementById("jnp-permission-warning");
        if (existing) return;

        var box = w.document.createElement("div");
        box.id = "jnp-permission-warning";
        box.style.position = "fixed";
        box.style.top = "20px";
        box.style.left = "20px";               // <-- left side
        box.style.zIndex = 99999;
        box.style.background = "rgba(255, 245, 210, 0.98)";
        box.style.color = "#222";
        box.style.padding = "10px 14px";
        box.style.borderRadius = "6px";
        box.style.boxShadow = "0 2px 8px rgba(0,0,0,0.18)";
        box.style.fontFamily = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif";
        box.style.fontSize = "13px";
        box.style.maxWidth = "360px";
        box.style.lineHeight = "1.25";

        var title = w.document.createElement("div");
        title.style.fontWeight = "600";
        title.style.marginBottom = "6px";
        title.textContent = "jupyternotifyplus: notifications disabled";

        var origin = (w.location && w.location.origin) ? w.location.origin : "this site";

        var message = w.document.createElement("div");
        message.style.marginBottom = "8px";

        var perm = (w.Notification && w.Notification.permission) ? w.Notification.permission : "unsupported";

        if (perm === "default") {
            message.textContent = "Notifications are not allowed yet. Click Request to ask the browser for permission.";
        } else if (perm === "denied") {
            message.textContent = "Notifications are blocked for " + origin + ". Enable them via the lock icon → Site settings → Notifications → Allow.";
        } else {
            message.textContent = "Notifications are not available in this browser.";
        }

        var btns = w.document.createElement("div");
        btns.style.display = "flex";
        btns.style.gap = "8px";

        if (perm === "default") {
            var req = w.document.createElement("button");
            req.textContent = "Request";
            req.style.cursor = "pointer";
            req.style.padding = "6px 10px";
            req.style.border = "none";
            req.style.borderRadius = "4px";
            req.style.background = "#0b66ff";
            req.style.color = "white";
            req.onclick = function() {
                try {
                    w.Notification.requestPermission().then(function(p) {
                        if (p === "granted") {
                            showToast("Notifications enabled", "You will now receive desktop notifications.");
                            if (box.parentNode) box.parentNode.removeChild(box);
                        } else if (p === "denied") {
                            showToast("Notifications blocked", "Permission denied. Use site settings to re-enable.");
                            message.textContent = "Notifications are blocked for " + origin + ". Enable them via the lock icon → Site settings → Notifications → Allow.";
                        }
                    }).catch(function() {
                        showToast("Request failed", "Could not request permission from the browser.");
                    });
                } catch (e) {
                    showToast("Request failed", "Could not request permission from the browser.");
                }
            };
            btns.appendChild(req);
        }

        var dismiss = w.document.createElement("button");
        dismiss.textContent = "Dismiss";
        dismiss.style.cursor = "pointer";
        dismiss.style.padding = "6px 10px";
        dismiss.style.border = "none";
        dismiss.style.borderRadius = "4px";
        dismiss.style.background = "#e0e0e0";
        dismiss.onclick = function() {
            if (box.parentNode) box.parentNode.removeChild(box);
        };
        btns.appendChild(dismiss);

        box.appendChild(title);
        box.appendChild(message);
        box.appendChild(btns);

        w.document.body.appendChild(box);

        // Auto-fade after 10s if not interacted with
        setTimeout(function() {
            if (box.parentNode) {
                box.style.transition = "opacity 0.4s ease";
                box.style.opacity = "0";
                setTimeout(function() {
                    if (box.parentNode) box.parentNode.removeChild(box);
                }, 400);
            }
        }, 10000);
    }

    // Startup check using top window
    if (typeof w !== "undefined" && "Notification" in w) {
        try {
            if (w.Notification.permission !== "granted") {
                showPermissionWarning();
            }
        } catch (e) {
            console.log("jupyternotifyplus: permission check failed", e);
        }
    }

    // --- Replace the startup check with this (use w.Notification) ---
    if (typeof w !== "undefined" && "Notification" in w) {
        try {
            if (w.Notification.permission !== "granted") {
                showPermissionWarning();
            }
        } catch (e) {
            // fallback: if anything goes wrong, do nothing
            console.log("jupyternotifyplus: permission check failed", e);
        }
    }

    w.notifyMe = function(title, body, iconUrl) {
        try {
            // Classic Jupyter Notebook: kernel is null during notebook load
            if (window.IPython &&
                IPython.notebook &&
                !IPython.notebook.kernel) {
                console.log("notifyMe: Kernel not ready, skipping notification (likely notebook restore).");
                return;
            }
        } catch (e) {
            console.log("notifyMe: error checking kernel state:", e);
            return;
        }

        if (!("Notification" in w)) {
            console.log("Browser does not support notifications, using toast fallback.");
            showToast(title, body);
            return;
        }

        if (Notification.permission === "default") {
            Notification.requestPermission();
        }

        if (Notification.permission === "granted") {
            new Notification(title, { body: body, icon: iconUrl });
        } else {
            console.log("Notification permission not granted, using toast fallback.");
            showPermissionWarning();
        }
    };

    console.log("notifyMe installed globally:", typeof w.notifyMe);
})();
"""

# Preset definitions
PRESETS = {
    "success": {
        "title": "Success",
        "message": "Operation completed successfully",
        "icon": "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/2705.png"
    },
    "failure": {
        "title": "Failure",
        "message": "An error occurred",
        "icon": "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/274c.png"
    },
    "error": {
        "title": "Error",
        "message": "An error occurred",
        "icon": "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/274c.png"
    },
    "warn": {
        "title": "Warning",
        "message": "Please check this",
        "icon": "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/26a0.png"
    }
}


@magics_class
class NotifyMeMagics(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self._pending_args = None

        publish_display_data(
            data={"application/javascript": _INIT_JS},
            metadata={}
        )

    def _resolve(self, value):
        if value is None:
            return None

        ns = self.shell.user_ns

        # Case 1: variable name
        if value in ns:
            return ns[value]

        # Case 2: f-string with stripped quotes (shlex behavior)
        if value.startswith("f") and ("{" in value or "=" in value):
            inner = value[1:]
            try:
                return eval(f"f'{inner}'", ns)
            except Exception:
                try:
                    return eval(f'f"{inner}"', ns)
                except Exception:
                    return value

        # Case 3: f-string with quotes intact
        if (value.startswith('f"') and value.endswith('"')) or \
           (value.startswith("f'") and value.endswith("'")):
            try:
                return eval(value, ns)
            except Exception:
                return value

        # Case 4: general expression
        try:
            return eval(value, ns)
        except Exception:
            return value

    @line_magic
    def notifyme(self, line):
        try:
            tokens = shlex.split(line)
        except ValueError:
            tokens = line.split()

        inline = False
        if tokens and tokens[0] == "here":
            inline = True
            tokens = tokens[1:]

        preset = None
        if tokens and tokens[0] in PRESETS:
            preset = PRESETS[tokens[0]]
            tokens = tokens[1:]

        parser = argparse.ArgumentParser(prog="%notifyme", add_help=False)
        parser.add_argument("-o", action="store_true")
        parser.add_argument("-t", type=str, default=None)
        parser.add_argument("-m", type=str, default=None)
        parser.add_argument("--icon", type=str, default=None)

        try:
            args = parser.parse_args(tokens)
        except SystemExit:
            return

        title = (
            self._resolve(args.t)
            or (preset["title"] if preset else "Cell finished")
        )
        message = (
            self._resolve(args.m)
            or (preset["message"] if preset else "Your cell has completed.")
        )
        icon = args.icon or (preset["icon"] if preset else DEFAULT_ICON)

        if inline:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{message} — At {timestamp}"

            js = f"""
            (function() {{
                if (window.IPython && IPython.notebook && !IPython.notebook.kernel) {{
                    console.log("Skipping inline notification: kernel not ready.");
                    return;
                }}
                var w = window;
                while (w !== w.parent) {{ w = w.parent; }}
                w.notifyMe({title!r}, {message!r}, {icon!r});
            }})();
            """

            publish_display_data(
                data={"application/javascript": js},
                metadata={}
            )
            return

        args.t = title
        args.m = message
        args.icon = icon
        # Store pending args privately to not persist in the notebook
        self._pending_args = args

    def post_run_cell(self, result):
        args = self._pending_args
        self._pending_args = None
        if not args:
            return

        args.t = self._resolve(args.t)
        args.m = self._resolve(args.m)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{args.m} — Finished at {timestamp}"

        if args.o:
            out = result.result
            if out is None:
                message += " (no output)"
            else:
                message += f" | Output: {str(out)[:200]}"

        js = f"""
        (function() {{
            // Only execute if the notebook kernel is actually running/ready
            // or if this is a fresh manual execution.
            if (window.IPython && IPython.notebook && !IPython.notebook.kernel) {{
                console.log("Skipping post-run notification: kernel not ready.");
                return;
            }}

            var w = window;
            while (w !== w.parent) {{ w = w.parent; }}
            
            if (typeof w.notifyMe === 'function') {{
                w.notifyMe({args.t!r}, {message!r}, {args.icon!r});
            }}
        }})();
        """

        publish_display_data(
            data={"application/javascript": js},
            metadata={}
        )

    def _make_inline_js(self, title, message, icon):
        return f"""
        (function() {{
            if (window.IPython && IPython.notebook && !IPython.notebook.kernel) {{
                console.log("Skipping inline notification: kernel not ready.");
                return;
            }}
            var w = window;
            while (w !== w.parent) {{ w = w.parent; }}
            w.notifyMe({title!r}, {message!r}, {icon!r});
        }})();
        """

    def _make_postrun_js(self, title, message, icon):
        return f"""
        (function() {{
            if (window.IPython && IPython.notebook && !IPython.notebook.kernel) {{
                console.log("Skipping post-run notification: kernel not ready.");
                return;
            }}
            var w = window;
            while (w !== w.parent) {{ w = w.parent; }}
            w.notifyMe({title!r}, {message!r}, {icon!r});
        }})();
        """


def load_ipython_extension(ipython):
    magics = NotifyMeMagics(ipython)
    ipython.register_magics(magics)

    # Force JS execution by emitting a visible output cell
    display(Javascript(_INIT_JS))

    ipython.events.register("post_run_cell", magics.post_run_cell)
    ipython.notifyme_magics = magics
