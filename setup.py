from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

ext = "pyx"

setup(
    name = 'fastbit',
    version = '1.0.0',
    ext_modules = [
        Extension('fastbit._fastbit', ['fastbit/_fastbit.' + ext],
        libraries = ["fastbit"],
       #library_dirs = ["/usr/local/lib"],
                  include_dirs=[np.get_include()]
        )
    ],
    cmdclass = {'build_ext': build_ext},
    packages = ["fastbit"],
    package_dir = {"fastbit": "fastbit"},
)
