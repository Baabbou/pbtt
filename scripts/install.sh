#!/bin/bash

if [ "$UID" -ne 0 ]; then
    echo "You must run this script as root user."
    exit 1
fi 

python -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r requirements.txt

pyinstaller --onefile --clean pbtt.py

cp dist/pbtt /usr/bin/pbtt 
cp dist/pbtt /usr/local/bin/pbtt

rm -rf pbtt.spec build dist .venv  

echo " "
echo "PBTT was correctly installed in /usr/bin/pbtt and /usr/local/pbtt"
