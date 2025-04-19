# okada4py

Okada implementation in Python

## Citation

This is a python implementation of the solution proposed by Okada in 1992. Please cite:

Okada, Y. (1992), Internal deformation due to shear and tensile faults in a half-space, Bulletin of the Seismological Society of America, 82(2), 1018–1040.

## Introduction

This repository is a modified version for modern installation of the [okada4py](https://github.com/jolivetr/okada4py) package written by Romain Jolivet. The modifications include:

1. Adding an `okada4py` folder and an `__init__.py` file in the `src` directory.
2. Adding the `init_numpy` function and related calls in the `okada92_py3.cpp` file to initialize NumPy.

These changes were made to ensure compatibility and proper initialization of NumPy within the package.


## Installation Guide for `okada4py`

This guide describes how to build and install the `okada4py` package, including necessary dependencies and platform-specific setup. It supports Python 3.7 and above.

---

### 1. Requirements

- Python ≥ 3.7
- `build`, `setuptools`, and `wheel` packages:
  ```bash
  pip install build setuptools wheel
  ```

---

### 2. Platform-Specific Setup

#### 🔧 **Windows (MSVC toolchain required)**

To compile C++ extensions on Windows, you must install **Microsoft C++ Build Tools**. Follow these steps:

**a. Download and Install Build Tools**
Visit: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Click **“Download Build Tools”** and run the installer.

**b. During installation, make sure to check the following components:**

✅ **C++ build tools** (main workload)✅ **MSVC v143 or v142 – VS 2022/2019 C++ x64/x86 build tools**✅ **Windows 10 SDK** or **Windows 11 SDK**✅ **CMake tools for Windows** (required by some C++ projects)

> 💡 **Recommended SDK versions**:
> Use stable versions such as:
> – `10.0.22621.0` (Windows 11 22H2)
> – `10.0.19041.0` (Windows 10)
>
> ⚠️ Avoid Insider Preview versions like `10.0.26100.0`, which may cause compatibility issues.

**c. Post-installation**

Cnfirm the compiler is available with:

```bash
cl
```

You are now ready to build C++-based Python packages.

---

#### 🐧 **Linux/macOS**

On Unix-based systems, ensure a working C++ compiler is installed, such as:

- **Linux:** `g++`, `cmake`, and developer headers (`build-essential` on Debian/Ubuntu)
- **macOS:** Xcode command line tools (`xcode-select --install`)

---

### 3. Build the Package

Once dependencies are satisfied, build the package from the project root:

```bash
python -m build
```

This will generate a `.whl` file in the `dist/` directory, for example:

```
dist/okada4py-12.0.2-py3-none-any.whl
```

---

### 4. Install the Package

Install the generated wheel file with `pip`. Replace `okada4py-12.0.2-py3-none-any.whl` with the actual name of the .whl file generated in the previous step:

```bash
pip install dist/okada4py-12.0.2-py3-none-any.whl
```

---

### 5. Verify Installation

Check that the package is properly installed:

```python
import okada4py
```

You can also verify the installation path using:

```bash
pip show -f okada4py
```

---

## ✅ Summary

This installation process uses the modern `pyproject.toml` and standard `wheel` format to ensure compatibility with current Python packaging standards.

- Windows users must install MSVC and SDKs as described.
- Linux/macOS users must have a working C++ compiler.
- All builds are performed with:
  ```bash
  python -m build
  ```
