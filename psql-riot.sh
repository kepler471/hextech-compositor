#!/bin/bash

# Simple shell script to connect to PostgreSQL
# Tested on:
# Linux Fedora 5.3.12-300.fc31.x86_64 #1 SMP Thu Nov 21 22:52:07 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
# Linux Ubuntu 18.04.4 LTS (Bionic Beaver) KEPLER-47-1 4.4.0-18362-Microsoft #476-Microsoft GNU/Linux

psql -h 127.0.0.1 -p 5432 -U postgres -d riot
# TODO in bash script, load db setup file "db_setup.sql"