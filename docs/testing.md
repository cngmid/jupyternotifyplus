# Testing

Tests are written using `pytest`.

Windows-specific issues with IPython history are handled by:

```python
os.environ["IPYTHON_HISTORY"] = "0"
ip.history_manager.enabled = False
```

```bash
pytest
```

All tests should pass cleanly on Windows, macOS, and Linux.

---