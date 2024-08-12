#!/bin/bash

if [ "$UID" -ne 0 ]; then
    echo "You must run this script as root user."
    exit 1
fi 

rm -rf /usr/bin/pbtt /usr/local/bin/pbtt
