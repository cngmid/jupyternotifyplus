# Usage Overview

Once loaded:

```python
%load_ext jupyternotifyplus
```

You have two main commands:
- `%notifyme` — triggers a notification after the cell finishes
- `%notifyme here` — triggers a notification immediately at that line

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

---