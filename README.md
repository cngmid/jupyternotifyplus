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

