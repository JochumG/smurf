# Bridging the poort 1234 from IFTTT to MQQT publishers.
#loading on startup Raspberry
# add in /etc/sc.local file:
# nohup python /home/pismurf/bridge/server.py &

#starting MQQT server
#docker stop $(docker ps -a -q)
#A. docker run --name mqtt --restart=always --net=host -tid -v /volume1/docker/mqtt/config:/mqtt/config:ro -v /volume1/docker/mqtt/log:/mqtt/log -v /volume1/docker/mqtt/data/:/mqtt/data/ toke/mosquitto
#B. docker run --name mqtt --restart=unless-stopped --net=host -tid -v /volume1/docker/mqtt/config:/mqtt/config:ro -v /volume1/docker/mqtt/log:/mqtt/log -v /volume1/docker/mqtt/data/:/mqtt/data/ toke/mosquitto


# webserver ding 
#import time (vermoedelijk voor de sleep functie)
from bottle import route, run, template

# MQQT ding
import paho.mqtt.publish as publish
#should be environment settings!
MQTT_SERVER = "77.248.61.13"
MQTT_PATH="none"
MQTT_COMMAND="none"

#Subscription paths
MQTT_PATH_Deebot = "deebot"
MQTT_PATH_Waterpomp = "pomp"

#bridging to MQQT publishing
# Handle http requests to the root address
@route('/')
def index():
 return 'Command not found'
 
# Handle http requests to /pomp
@route('/pomp/:action')
def pomp(action=0):
 MQTT_PATH=MQTT_PATH_Waterpomp
 MQTT_COMMAND=action
 publish.single(MQTT_PATH,MQTT_COMMAND, hostname=MQTT_SERVER)

# Handle http requests to /deebot
@route('/deebot/:action')
def deebot(action=0):
 MQTT_PATH=MQTT_PATH_Waterpomp
 MQTT_COMMAND=action
 publish.single(MQTT_PATH,MQTT_COMMAND, hostname=MQTT_SERVER)

run(host='0.0.0.0', port=80)
