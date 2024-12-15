#!/bin/bash

$cd /home/ubuntu/TWS_Study_material


echo "THSI IS THE GIT STATUS"
echo "$(git status)"
if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi

echo "GIT ADD STARTED"
$(git add .)
if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi

echo "GIT COMMIT STARTED"
echo "$(git commit -m "$(date '+%Y-%m-%d-%H-%M-%S')")"
if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi
echo "GIT PUSH STARTED"
echo "$(git push -u origin main)"
if [ $? -eq 0 ]; then
        echo "----------DONE----------"
else
        echo "----------ERROR----------"
fi

