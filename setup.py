from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='sample_c_extension',
    setup_requires=['Cython'],
    ext_modules=cythonize('hello.pyx')
)