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
%notifyme here
```

Triggers a notification immediately.

```python
%notifyme here -t "Checkpoint" -m "Step 1 done"
```

---

