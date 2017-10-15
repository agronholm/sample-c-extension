# coding: utf-8
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='sample_c_extension',
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag'
    },
    author=u'Alex Grönholm',
    author_email='alex.gronholm@nextday.fi',
    ext_modules=cythonize('hello.pyx'),
    setup_requires=['setuptools_scm'],
    extras_require={
        'test': ['pytest']
    }
)