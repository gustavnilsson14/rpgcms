#!/bin/bash
time=$(date +"%Y-%m-%d_%H-%m-%S")
mysqldump -h 127.0.0.1 -u rpg -prpggpr rpg --no-create-info --complete-insert > db_backups/dump_$time.sql
python server.py
