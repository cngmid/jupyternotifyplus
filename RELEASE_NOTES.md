## 0.4.2 — Fix notifications firing on notebook load

### Bug fix:

Opening a notebook could trigger old notifications because classic
Jupyter Notebook replays JavaScript outputs before the kernel starts.

### Fix:

All notification JavaScript now checks whether the kernel is ready:

```javascript
if (window.IPython && IPython.notebook && !IPython.notebook.kernel) {
    return;
}
```

This prevents notifications from firing during notebook restore.

### Other improvements:

- Cleaner JS injection
- More robust inline and post‑run notifications
- Tests updated to cover restore behavior