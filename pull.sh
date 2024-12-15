#!/bin/bash

echo "GIT REBASE"

echo "$(git rebase)"

if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi

echo "GIT FETCH"

echo "$(git fetch)"

if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi

echo "GIT PULL"

echo "$(git pull)"

if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi

