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