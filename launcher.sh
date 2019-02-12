#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pismurf/code/bridge/
sudo python server.py &
cd /
cd /home/pismurf/code/sub/sub_listener
sudo python deebot_subscriber.py &
sudo python water_subscriber.py &
cd /
