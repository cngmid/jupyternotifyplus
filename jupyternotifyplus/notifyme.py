import argparse
import shlex
from datetime import datetime
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.display import publish_display_data

# Default icon
DEFAULT_ICON = "https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/2139.png"

# JavaScript injected into the notebook
_INIT_JS = r"""
(function() {
    var w = window;
    while (w !== w.parent) {
        w = w.parent;
    }

    w.notifyMe = function(title, body, iconUrl) {
        if (!("Notification" in w)) {
            console.log("Browser does not support notifications.");
            return;
        }

        if (Notification.permission === "default") {
            Notification.requestPermission();
        }

        if (Notification.permission === "granted") {
            new Notification(title, { body: body, icon: iconUrl });
        } else {
            console.log("Notification permission not granted.");
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
            inner = value[1:]  # remove leading f
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

        title = self._resolve(args.t) or (preset["title"] if preset else "Cell finished")
        message = self._resolve(args.m) or (preset["message"] if preset else "Your cell has completed.")
        icon = args.icon or (preset["icon"] if preset else DEFAULT_ICON)

        if inline:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{message} — At {timestamp}"

            js = f"""
            (function() {{
                var w = window;
                while (w !== w.parent) {{
                    w = w.parent;
                }}
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
        self.shell.user_ns["_notifyme_args"] = args

    def post_run_cell(self, result):
        args = self.shell.user_ns.pop("_notifyme_args", None)
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
            var w = window;
            while (w !== w.parent) {{
                w = w.parent;
            }}
            w.notifyMe({args.t!r}, {message!r}, {args.icon!r});
        }})();
        """

        publish_display_data(
            data={"application/javascript": js},
            metadata={}
        )


def load_ipython_extension(ipython):
    magics = NotifyMeMagics(ipython)
    ipython.register_magics(magics)
    ipython.events.register("post_run_cell", magics.post_run_cell)
