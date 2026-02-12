# Jupyter Notify Plus

![badge](https://img.shields.io/badge/Jupyter-Notify%20Plus-blue?style=for-the-badge&logo=jupyter)

**Jupyter Notify Plus** is a lightweight, powerful extension that adds:

- `%notifyme` — end-of-cell notifications  
- `%notifyme here` — inline notifications  
- Presets: `success`, `warn`, `error`, `failure`  
- Custom icons, timestamps, and output inclusion  
- Works in classic Notebook and JupyterLab  

---

## Why this exists

Long-running notebook cells deserve better feedback.  
This extension gives you clean, modern browser notifications without any external dependencies.

---

## Quick Example

```python
%load_ext jupyternotifyplus

%notifyme success -t "Done" -m "Futures updated"

%notifyme here warn "Starting download"
download_data()
```

## Features

- 🔔 Inline notifications
- 🧭 End-of-cell notifications
- 🎨 Preset icons and styles
- 🧪 Fully tested (Windows-safe)
- 📦 Installable via pip
- 🧰 Zero dependencies

---

# 🧩 3. `docs/installation.md`

# Installation

## Install from source

```bash
pip install jupyternotifyplus
```

Or from a local checkout:
```bash
pip install -e .
```

## Load the extension

In any Jupyter Notebook:
```python
%load_ext jupyternotifyplus
```

You’re ready to go.

---

# 🧩 4. `docs/usage.md`

```markdown
# Usage Overview

Once loaded:

```python
%load_ext jupyternotifyplus
```

You have two main commands:
- `%notifyme` — triggers a notification **after** the cell finishes
- `%notifyme here` — triggers a notification **immediately** at that line

---

## End-of-cell notification

```python
%notifyme -t "Done" -m "Cell finished"
```

---

## Inline notification

```python
%notifyme here -t "Checkpoint" -m "Reached step 1"
```

You can use as many inline notifications as you want.
```

---

# 🧩 5. `docs/magics.md`

```markdown
# Magic Commands

## `%notifyme`

Triggers a notification after the cell completes.

### Options

| Option | Description |
|--------|-------------|
| `-t`   | Title       |
| `-m`   | Message     |
| `-o`   | Include output in message |
| `--icon` | Custom icon URL |

### Example

```python
%notifyme -t "Finished" -m "Processing complete"
```

---

`%notifyme here`

Triggers a notification immediately.
```python
%notifyme here -t "Checkpoint" -m "Step 1 done"
```

---

# 🧩 6. `docs/presets.md`

```markdown
# Presets

Presets provide default title, message, and icon.

Available presets:

- `success`
- `warn`
- `error`
- `failure`

---

## Inline presets

```python
%notifyme here success "Step completed"
%notifyme here warn "Something odd happened"
```

---

## End-of-cell presets

```python
%notifyme success
%notifyme failure
```

---

## Presets with overrides

```python
%notifyme success -t "Download complete" -m "Futures updated"
```

---

# 🧩 7. `docs/development.md`

# Development

Clone the repository:

```bash
git clone https://github.com/yourname/jupyternotifyplus
cd jupyternotifyplus
```

Install in editable mode:

```bash
pip install -e .[dev]
```

Run tests:
```bash
pytest
```

Build the package:

```bash
python -m build
```

---

# 🧩 8. `docs/testing.md`

# Testing

Tests are written using `pytest`.

Windows-specific issues with IPython history are handled by:

```python
os.environ["IPYTHON_HISTORY"] = "0"
ip.history_manager.enabled = False
```

Run tests:

```bash
pytest
```

All tests should pass cleanly on Windows, macOS, and Linux.

---

# 🧩 9. `docs/changelog.md`

# Changelog

## 0.1.0

- Initial release
- End-of-cell notifications
- Inline notifications
- Presets (`success`, `warn`, `error`, `failure`)
- Windows-safe test suite
- Packaging and versioning
