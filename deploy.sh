#!/bin/bash
python setup.py sdist
twine check dist/*
twine upload dist/*
