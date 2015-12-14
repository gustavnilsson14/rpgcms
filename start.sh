#!/bin/bash

sudo iptables -A INPUT -i wlan0 -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -i wlan0 -p tcp --dport 1337 -j ACCEPT
sudo iptables -A PREROUTING -t nat -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 1337

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    echo "Backing up db!"
    time=$(date +"%Y-%m-%d_%H-%M-%S")
    mysqldump -h 127.0.0.1 -u rpg -prpggpr rpg --no-create-info --complete-insert > db_backups/dump_$time.sql
    rm db_backups/dump_previous.sql
    mv db_backups/dump_latest.sql db_backups/dump_previous.sql
    cp db_backups/dump_$time.sql db_backups/dump_latest.sql
    echo "Backup complete"
}

python server.py 1
