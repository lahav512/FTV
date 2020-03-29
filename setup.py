from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("AppPackage/Experiments/CythonTests/helloworld.pyx", compiler_directives={'language_level' : "3"},
        install_requires=['wrapt'], install_requires=['wrapt'])
)