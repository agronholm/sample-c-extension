from setuptools import setup
from Cython.Build import cythonize

setup(
    name='sample_c_extension',
    ext_modules=cythonize('hello.pyx')
)