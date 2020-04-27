from Cython.Build import cythonize
from setuptools import setup


setup(
    ext_modules = cythonize("AppPackage/Experiments/CythonTests/helloworld.pyx", compiler_directives={'language_level' : "3"},
        install_requires=['wrapt'], install_requires=['wrapt'], install_requires=['requests'],
        install_requires=['requests'])
)