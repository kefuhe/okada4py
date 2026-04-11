from pathlib import Path

import numpy as np
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext as build_ext_orig


ROOT = Path(__file__).parent
README = (ROOT / "README.md").read_text(encoding="utf-8")

# Simplify NumPy include directory acquisition
npinclude = np.get_include()

# Where are the includes
include_dirs = ["src/", npinclude]

# Which are the sources
sources = [
    "src/dc3d.cpp",
    "src/disloc3d.cpp",
    "src/okada92_py3.cpp",
]

# Additional flags
CFLAGS = []

# Create an extension
ext_modules = [
    Extension(
        "okada4py._okada92",
        sources=sources,
        include_dirs=include_dirs,
        extra_compile_args=CFLAGS,
    )
]


# Custom build_ext command to ensure include paths are set correctly
class build_ext(build_ext_orig):
    def build_extensions(self):
        for ext in self.extensions:
            ext.include_dirs = include_dirs
        super().build_extensions()


setup(
    name="okada4py",
    version="12.0.2",
    description="Python bindings for the Okada (1992) elastic half-space solution",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["okada4py"],
    package_dir={"okada4py": "src/okada4py"},
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    install_requires=["numpy"],
    python_requires=">=3.7",
    include_package_data=True,
    license="GPL-3.0-or-later",
    license_files=["LICENSE"],
    url="https://github.com/jolivetr/okada4py",
    project_urls={
        "Upstream": "https://github.com/jolivetr/okada4py",
    },
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: C++",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
)
