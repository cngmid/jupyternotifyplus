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

## Variable and Expression Resolution
`%notifyme` supports **Python variable names**, **expressions**,
and **f‑strings** inside the `-t` (title) and `-m` (message) arguments.

This allows you to write expressive, dynamic notifications without
string‑escaping or manual formatting.

### Examples

### Using variables

```python
a = "Hello World"
%notifyme success -t a
```

The notification title becomes:

```
Hello World
```

### Using f‑strings

```python
%notifyme success -t f"1+1={1+1}"
```

Title:

```
1+1=2
```

### Using expressions

```python
%notifyme -t "3 * 7"
```

Title:

```
21
```

### Resolution Rules

`%notifyme` resolves values using the following logic:

1. If the argument matches a variable name in the user namespace, its value is used.

2. Otherwise, the argument is evaluated as a Python expression (e.g., f‑strings, arithmetic).

3. If evaluation fails, the literal string is used unchanged.

This makes `%notifyme` flexible while remaining safe and predictable.

---