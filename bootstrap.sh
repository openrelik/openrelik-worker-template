#!/bin/bash
# This small script will bootstrap the new worker code.
echo "Please answer the below question to bootstrap your initial worker code."
echo
echo -n "Workername? "
read workername
echo -n "Your name? "
read yourname
echo -n "Your email address? "
read youremail
echo -n "A short one line description of the worker? "
read onelinedescription

sed -i.backup "s/TEMPLATEWORKERNAME/$workername/g" pyproject.toml
sed -i.backup "s/TEMPLATENAME/$yourname/g" pyproject.toml
sed -i.backup "s/TEMPLATEEMAIL/$youremail/g" pyproject.toml
sed -i.backup "s/TEMPLATEWORKERNAME/$workername/g" src/tasks.py
sed -i.backup "s/TEMPLATEDESC/$onelinedescription/g" src/tasks.py
sed -i.backup "s/TEMPLATEWORKERNAME/$workername/g" README.md

rm -r ./*.backup
