#! /bin/bash

# Simple shell script to connect to the Windows 10 PostgreSQL 11 Database Server.
# Linux Ubuntu 18.04.4 LTS (Bionic Beaver) KEPLER-47-1 4.4.0-18362-Microsoft #476-Microsoft GNU/Linux

psql -h 127.0.01 -p 5432 -U postgres -d riot