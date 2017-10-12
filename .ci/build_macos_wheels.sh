#!/usr/bin/env bash

set -e

brew update
brew outdated pyenv || brew upgrade pyenv
export PATH=~/.pyenv/shims:$PATH
for PYVER in "2.7.14" "3.4.7" "3.5.4" "3.6.3"; do
  pyenv install ${PYVER}
  pyenv global ${PYVER}
  python -m pip install Cython wheel
  python setup.py bdist_wheel
done
