#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pismurf/code
sudo python /bridge/server.py
sudo python /sub/sub_listener/deebot_subscriber.py
sudo python /sub/sub_listener/water_subscriber.py
cd /
