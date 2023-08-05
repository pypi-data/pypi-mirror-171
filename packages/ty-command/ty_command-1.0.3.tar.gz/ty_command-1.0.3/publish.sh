#!/usr/bin/env bash
set -eou pipefail
rm -rf dist
py -m venv venv
source venv/bin/activate
py -m pip install --upgrade build
py -m build
py -m pip install --upgrade twine
py -m twine upload dist/*
deactivate
rm -rf venv
