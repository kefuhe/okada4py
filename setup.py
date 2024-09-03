from setuptools import setup, Extension
import numpy as np
import sys

# Simplify NumPy include directory acquisition
npinclude = np.get_include()

# Where are the includes
include_dirs = ['src/', npinclude]

# Which are the sources
sources = ['src/dc3d.cpp', 'src/disloc3d.cpp']

majorVersion = sys.version_info[0]
if majorVersion == 2:
    sources.append('src/okada92.cpp')
elif majorVersion == 3:
    sources.append('src/okada92_py3.cpp')
else:
    print('Unknown version of Python: Version {}'.format(majorVersion))
    sys.exit(1)

# Additional flags
CFLAGS = []

# Create an extension
ext_modules = [Extension('okada4py._okada92', 
            sources=sources, 
            include_dirs=include_dirs,
            extra_compile_args=CFLAGS)]

# Main
setup(
    name='okada4py',
    version='12.0.2',
    packages=['okada4py'],
    package_dir={'okada4py': 'src/okada4py'},
    ext_modules=ext_modules,
)