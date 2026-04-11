# okada4py

Python bindings for the Okada (1992) solution for displacement, strain, and stress in an elastic half-space.

This repository is a packaging-oriented fork of the original [okada4py](https://github.com/jolivetr/okada4py) package written by Romain Jolivet. In particular, it includes:

1. a `src/okada4py` package with `__init__.py`, so the compiled extension can be imported as `okada4py`
2. NumPy initialization updates in `okada92_py3.cpp` for modern Python 3 builds

This project is not a pure-Python package: it builds a compiled extension module. Installation may therefore require a working C/C++ toolchain, especially on Windows when no matching wheel is available.

## Citation 📚

Please cite the original paper:

Okada, Y. (1992), Internal deformation due to shear and tensile faults in a half-space, Bulletin of the Seismological Society of America, 82(2), 1018-1040.

## Support Status ✅

- Expected Python support: `>= 3.7`
- Preliminary testing completed in conda-managed environments on:
  - Windows
  - Ubuntu / Linux
- macOS is intended to work from source with standard developer tools, but is currently less tested than Windows and Ubuntu

The `>= 3.7` statement is based on initial testing and the current source layout. It should be treated as expected support rather than an exhaustive compatibility guarantee across all Python, compiler, and architecture combinations.

## Installation 🔧

All installation commands below install into the currently active Python environment. The recommended default is to use a user-managed environment, for example a conda environment. This is also the setup used for the current Windows and Ubuntu tests.

If you use conda, a typical workflow is:

```bash
conda create -n okada4py python=3.10
conda activate okada4py
python -m pip install -U pip setuptools wheel build numpy
```

If you prefer `venv` or another environment manager, the same install commands still apply after that environment is activated.

There are two common installation paths:

1. install a matching prebuilt wheel
2. build from source

### Common Prerequisites

- Python `>= 3.7`
- `pip`
- `numpy`

It is usually safest to upgrade the packaging tools first in the active environment:

```bash
python -m pip install -U pip setuptools wheel build numpy
```

## Install From a Wheel 📦

If you already have a wheel file that matches your Python version and platform, this is the easiest path:

```bash
python -m pip install path/to/okada4py-<version>-<python-tag>-<abi-tag>-<platform-tag>.whl
```

Because this package contains a compiled extension, the wheel is platform-specific. For example:

```text
okada4py-12.0.2-cp310-cp310-win_amd64.whl
okada4py-12.0.2-cp310-cp310-linux_x86_64.whl
```

A wheel built for one Python version or platform will not install on another.

This repository intentionally allows tested wheel files in `dist/*.whl` to be published to GitHub so users can install them directly. Other build outputs in `dist/` are not intended to be tracked.

The GitHub build workflow is configured to build CPython wheels for Python 3.10, 3.11, and 3.12. The current target set is:

- Windows x86_64
- Linux x86_64
- macOS x86_64
- macOS arm64

## Build and Install From Source 🏗️

### Windows 🪟

Windows is the platform where installation failures are most likely, usually because the required C/C++ build tools are missing.

1. Install Microsoft C++ Build Tools from:
   [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. In the installer, select the C++ build tools workload. At minimum, make sure MSVC and a Windows SDK are installed.
3. Open a new terminal after installation. If you use conda, reopening `Anaconda Prompt` or a fresh shell and then running `conda activate <env>` is recommended. If available, `Developer PowerShell for VS 2022` or `x64 Native Tools Command Prompt` is also a reliable choice.
4. Install from the project root inside the activated environment:

```bash
python -m pip install .
```

If you want to build a wheel instead of installing directly:

```bash
python -m build
```

### Ubuntu / Linux 🐧

On Ubuntu or Debian-based systems, install a compiler toolchain and Python development headers first:

```bash
sudo apt-get update
sudo apt-get install -y build-essential python3-dev
```

Then activate your target environment, such as a conda environment, and install from the project root:

```bash
python -m pip install .
```

On other Linux distributions, install the equivalent C++ compiler and Python development packages.

### macOS 🍎

Install the Xcode command line tools first:

```bash
xcode-select --install
```

Then activate your target environment and install from the project root:

```bash
python -m pip install .
```

On Apple Silicon systems, make sure your Python interpreter and compiler toolchain are from the same architecture context. A conda environment or a `venv` environment are both reasonable choices here.

## Verify Installation 🔍

After installation, confirm that the package imports correctly from the active environment:

```bash
python -c "import okada4py; print(okada4py.__file__)"
```

You can also inspect the installed files with:

```bash
python -m pip show -f okada4py
```

## Minimal Usage Example 🚀

```python
import numpy as np
import okada4py as ok92

xs = np.array([0.0])
ys = np.array([0.0])
zs = np.array([0.0])

xc = np.array([0.0])
yc = np.array([0.0])
depth = np.array([2.0])
length = np.array([10.0])
width = np.array([6.0])
dip = np.array([45.0])
strike = np.array([0.0])

ss = np.array([1.0])
ds = np.array([0.0])
ts = np.array([0.0])

mu = 30.0e9
nu = 0.25

u, d, s, flag, flag2 = ok92.okada92(
    xs, ys, zs,
    xc, yc, depth, length, width, dip, strike,
    ss, ds, ts,
    mu, nu
)

print(u)
print(d)
print(s)
```

For a larger example, see `test/test.py`.

## Common Installation Problems 🛠️

### `Microsoft Visual C++ 14.0 or greater is required`

On Windows, this means the Visual Studio C++ build tools are not installed or are not visible from the current terminal session. Install the build tools from the Microsoft link above, open a new shell, reactivate the target environment, and retry.

### `... is not a supported wheel on this platform`

The wheel does not match your current Python version, ABI, operating system, or CPU architecture. Use a wheel built for your exact environment, or install from source.

### `No module named 'okada4py._okada92'`

The compiled extension was not built or installed successfully. This can also happen if you try to import directly from the source tree before the extension exists. Reinstall the package inside the intended environment and check the compiler/toolchain setup.

### NumPy header or import errors

If the build reports NumPy-related errors, make sure `numpy` is installed in the same Python environment that is being used for the build:

```bash
python -m pip install -U numpy
```

## Building and Publishing Distributions 📦

If you are maintaining the package and want to build source and wheel distributions:

```bash
python -m build
```

The generated files will be placed in `dist/`. Because this package contains a compiled extension, wheel filenames are platform- and Python-version-specific rather than `py3-none-any`.

In this repository, `dist/*.whl` is intentionally allowed to be tracked and published to GitHub for tested environments. `__pycache__` directories and other transient build outputs should not be committed.

A GitHub Actions workflow is included under `.github/workflows/build-wheels.yml`. It builds wheels for Python 3.10 to 3.12 across the target platforms above, uploads them as workflow artifacts, and publishes them to GitHub Releases when you push a tag such as `v12.0.2`.
