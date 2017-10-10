#!/usr/bin/env bash

set -e

for PYVER in "cp27-cp27mu" "cp34-cp34m" "cp35-cp35m" "cp36-cp36m"; do
  PYBIN="/opt/python/${PYVER}/bin"
  "${PYBIN}/pip" install Cython wheel
  "${PYBIN}/python" setup.py bdist_wheel
done