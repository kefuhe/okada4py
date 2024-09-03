# okada4py

## Installation

### 1. Project Structure

okada4py/
├── src/
│   ├── okada4py/
│   │   └── __init__.py
│   ├── dc3d.cpp
│   ├── disloc3d.cpp
│   └── okada92_py3.cpp
├── setup.py
└── pyproject.toml


### 2. Code Modifications

In the [`okada92_py3.cpp`] file, add the [`init_numpy`] function and related calls to initialize NumPy. Here is an excerpt of the modified code:

```cpp
#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "dc3d.h"
#include "disloc3d.h"
#include "Python.h"
#include <numpy/arrayobject.h>

int init_numpy() {
    import_array();
    return 0; 
}

static PyObject *py_Okada(PyObject *self, PyObject *args)
{
    if (init_numpy() != 0) {
        return NULL;  // numpy failed to initialize
    }
    // Arguments for disloc3d
    double *models;         // Dislocations [nmod x 10]: [length, width, depth, dip, strike, xc, yc, ss, ds, ts]
    int nmod;               // Number of dislocations
    double *stations;       // Stations [nstat x 3]: [xs, ys, zs]
    int nstat;              // Number of stations
    double mu;              // Shear modulus    (Used for stress computation)
    double nu;              // Poisson's ration
    double *uout;           // Displacements [nstat x 3]: [Ux, Uy, Uz]
    double *dout;           // Strains [nstat x 9]: [Uxx, Uxy, Uxz, Uyx, Uyy, Uyz, Uzx, Uzy, Uzz]
    double *sout;           // Stresses [nstat x 6]: [Sxx, Sxy, Sxz, Syy, Syz, Szz]
    double *flagout;        // A flag per station [nstat]
    double *flagout2;       // Another flag per station and per dislocation [nstat x nmod]

    // Equivalent in python
    PyArrayObject *Py_xs, *Py_ys, *Py_zs;   // Station positions
    PyArrayObject *Py_xc, *Py_yc, *Py_depth;// Dislocation position
    PyArrayObject *Py_length, *Py_width;    // Dislocation size
    PyArrayObject *Py_dip, *Py_strike;      // Dislocation orientation
    PyArrayObject *Py_ss, *Py_ds, *Py_ts;   // Strike-, Dip- and Tensile slip 

    // import python arguments and check
    import_array1(NULL);
    if (!PyArg_ParseTuple(args, "O!O!O!O!O!O!O!O!O!O!O!O!O!dd",
                &PyArray_Type, &Py_xs, 
                &PyArray_Type, &Py_ys, 
                &PyArray_Type, &Py_zs, 
                &PyArray_Type, &Py_xc, 
                &PyArray_Type, &Py_yc, 
                &PyArray_Type, &Py_depth,
                ...
```

### 3. Build the Wheel Package

Run the following command in the root directory of your project to build the wheel package:

```sh
python -m build
```

This will generate a `.whl` file, typically located in the [`dist/`] directory. The exact name of the `.whl` file will depend on your package version and Python version. For example, it might be something like `dist/okada4py-12.0.2-py3-none-any.whl`.

### 4. Install the Wheel Package

Use `pip` to install the generated `.whl` file. Replace `okada4py-12.0.2-py3-none-any.whl` with the actual name of the `.whl` file generated in the previous step:

```sh
pip install dist/okada4py-12.0.2-py3-none-any.whl
```

### 5. Verify Installation

After installation, verify that the `okada4py` package can be imported in Python:

```python
import okada4py
```

If the import is successful, the installation is complete.

## Summary

By following these steps, you can build and install the `okada4py` package using the modern [`pyproject.toml`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FE%3A%2Fgeocodes%2Fokada4py%2Fpyproject.toml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "e:\geocodes\okada4py\pyproject.toml") and `wheel` format. This ensures compatibility with current and future Python packaging standards.
