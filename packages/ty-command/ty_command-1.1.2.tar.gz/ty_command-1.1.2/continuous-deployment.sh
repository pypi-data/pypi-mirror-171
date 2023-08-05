#!/usr/bin/env bash
set -eou pipefail

if [[ $(pip list | grep -E '^ty-command\b' | python3 -c 'from fileinput import input; print([x for x in input()][0].split()[1])') == $(python3 -c 'from sys import path; path.insert(0, "./src/ty_command"); import ty; print(ty.__version__)') ]]; then
    echo New version not detected
else
    echo New version detected
    rm -rf dist
    py -m venv venv
    source venv/bin/activate
    py -m pip install --upgrade build
    py -m build
    py -m pip install --upgrade twine
    py -m twine upload dist/*
    deactivate
    rm -rf venv
fi
