#!/bin/bash
sed -i 's/version = "[0-9\.]*"/version = "'"$1"'"/g' pyproject.toml
sed -i 's/release = "[0-9\.]*"/release = "'"$1"'"/g' doc/source/conf.py
