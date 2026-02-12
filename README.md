![jupyternotifyplus](https://img.shields.io/badge/Jupyter-Notify%20Plus-blue?style=for-the-badge&logo=jupyter)

![version](https://img.shields.io/pypi/v/jupyternotifyplus?style=flat-square)

![license](https://img.shields.io/badge/license-MIT-green)

![python](https://img.shields.io/badge/python-3.8%2B-blue)

# jupyternotifyplus

A powerful Jupyter Notebook extension that provides:

- `%notifyme` end-of-cell notifications  
- `%notifyme here` inline notifications  
- Presets: `success`, `warn`, `error`, `failure`  
- Custom icons, timestamps, and output inclusion  
- Works in classic Notebook and JupyterLab  

## Installation

```bash
pip install jupyternotifyplus
```

## Usage

```bash
%load_ext jupyternotifyplus.notifyme
```

Then:
```bash
%notifyme success
%notifyme here warn "Checkpoint reached"
```

---

## MIT License

Copyright (c) 2026 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
...
