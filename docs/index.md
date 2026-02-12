# Jupyter Notify Plus

Jupyter Notify Plus is a lightweight, powerful extension that adds:

- %notifyme — end-of-cell notifications
- %notifyme here — inline notifications
- Presets: success, warn, error, failure
- Custom icons, timestamps, and output inclusion
- Works in classic Notebook and JupyterLab

---

## Why this exists

Long-running notebook cells deserve better feedback. This extension gives you clean, modern browser notifications without any external dependencies.

---

## Quick Example

%load_ext jupyternotifyplus

%notifyme success -t "Done" -m "Futures updated"

%notifyme here warn "Starting download"
download_data()

---

## Features

- Inline notifications
- End-of-cell notifications
- Preset icons and styles
- Fully tested (Windows-safe)
- Installable via pip
- Zero dependencies
