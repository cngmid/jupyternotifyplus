# Jupyter Notify Plus

![jupyternotifyplus](https://img.shields.io/badge/Jupyter-Notify%20Plus-blue?style=for-the-badge&logo=jupyter)

[![PyPI Version](https://img.shields.io/pypi/v/jupyternotifyplus.svg)](https://pypi.org/project/jupyternotifyplus/)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build Status](https://github.com/cngmid/jupyternotifyplus/actions/workflows/publish.yml/badge.svg)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://cngmid.github.io/jupyternotifyplus?ref=readme)
![Downloads](https://img.shields.io/pypi/dm/jupyternotifyplus)

---

Jupyter Notify Plus enhances your notebook workflow with clean, modern inline notifications and end‑of‑cell alerts.  
It’s lightweight, intuitive, and designed to integrate seamlessly into your existing environment.

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

## License

MIT License

Copyright (c) 2026 Daniel Cangemi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

