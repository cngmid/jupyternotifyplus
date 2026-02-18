# Jupyter Notify Plus — Release 0.4.1

This release brings two important improvements to the `%notifyme` magic,
making notifications more predictable and far more expressive.

---

## ✨ Smarter Titles & Messages

`%notifyme` now understands:

- **Variables**
- **f‑strings**
- **Python expressions**

Examples:

```python
a = "Hello World"
%notifyme success -t a

%notifyme success -t f"1+1={1+1}"
%notifyme -t "3 * 7"
```

If evaluation fails, the literal text is used — no surprises.

---

## 🔧 No More Notifications on Notebook Load

Previously, reopening a notebook that contained `%notifyme` calls could
trigger old notifications due to how Jupyter restores state.

This is now fixed:

- Notifications fire **only** after real cell execution
- No state leaks into the user namespace
- Notebook reloads are silent and predictable

---

## 🧪 Improved Test Coverage

The test suite now includes:

- Expression and f‑string resolution
- State‑clearing behavior
- Protection against stale notifications