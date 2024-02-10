#!/bin/bash
set -e

cd ./python

echo "Installing poetry version plugin"
pip install plugin/poetry-version-plugin

pyproject_files=$(find . -type f -name "pyproject.toml")
for file in ${pyproject_files[@]}
do
    folder=$(dirname "${file}")
    echo "moving into folder ${folder}"

    # Check if the folder contains "plugin" or if it is "plugin"
    if [[ ${folder} == *'plugin'* || ${folder} == 'plugin' ]]; then
        echo -e "\033[33mSkipping folder ${folder}\033[0m"
        continue
    fi
    pushd "${folder}"
        poetry lock --no-update
    popd

done
