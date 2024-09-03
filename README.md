# okada4py

Okada implementation in Python

## Citation

This is a python implementation of the solution proposed by Okada in 1992. Please cite:

Okada, Y. (1992), Internal deformation due to shear and tensile faults in a half-space, Bulletin of the Seismological Society of America, 82(2), 1018–1040.

## Introduction

This repository is a modified version of the original [okada4py](https://github.com/jolivetr/okada4py) package. The modifications include:

1. Adding an `okada4py` folder and an `__init__.py` file in the `src` directory.
2. Adding the `init_numpy` function and related calls in the `okada92_py3.cpp` file to initialize NumPy.

These changes were made to ensure compatibility and proper initialization of NumPy within the package.

## Installation

To install the `okada4py` package, follow these steps:

### 1. Build the Wheel Package

Run the following command in the root directory (`okada4py` here) of your project to build the wheel package:

```bash
python -m build
```

This will generate a `.whl` file, typically located in the [`dist/`]. The exact name of the `.whl` file will depend on your package version and Python version. For example, it might be something like `dist/okada4py-12.0.2-py3-none-any.whl`.

### 2. Install the Wheel Package

Use `pip` to install the generated `.whl` file. Replace `okada4py-12.0.2-py3-none-any.whl` with the actual name of the .whl file generated in the previous step:

```sh
pip install dist/okada4py-12.0.2-py3-none-any.whl
```

### 3. Verify Installation

After installation, verify that the `okada4py` package can be imported in Python:

```python
import okada4py
```

If the import is successful, the installation is complete.

## Summary

By following these steps, you can build and install the `okada4py` package using the modern [`pyproject.toml`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FE%3A%2Fgeocodes%2Fokada4py%2Fpyproject.toml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "e:\geocodes\okada4py\pyproject.toml") and `wheel` format. This ensures compatibility with current and future Python packaging standards.
