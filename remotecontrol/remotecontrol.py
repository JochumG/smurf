#Eerste deepbot actie script listener 28-01-3019
#KEEP this scipt running
#nohup sudo python /home/pismurf/code/remotecontrol/remotecontrol.py>/home/pismurf/code/logs/remotecontrol.log -d &


#https://www.instructables.com/id/How-To-Useemulate-remotes-with-Arduino-and-Raspber/
#een deebot lirc file maken
#https://raspberrypi.stackexchange.com/questions/81876/raspberry-pi-3-not-lirc-not-running-working
#de volgende url helemaal doorlopen om het werkend te krijgen, deze lijkt in zijn geheel correct
#https://github.com/mtraver/rpi-ir-remote


#deebot.lircd.conf
#sudo irrecord -d /dev/lirc0 ~/lircd.conf



import os
import paho.mqtt.client as mqtt
import random
#should be environment settings!
#MQTT_SERVER = "77.248.61.13"
MQTT_SERVER = "192.168.0.60"

#Subscription paths
MQTT_PATH = "deebot"

def logging(string):
 ts=datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
 print (ts+":"+string)
 
def on_connect(client, userdata, flags, rc):
    logging("Deebot Subscribed (code "+str(rc)+")")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	logging(msg.topic+" "+msg.payload)
	if msg.payload=="stop":
	   os.system("irsend SEND_ONCE deebot KEY_STOP")
	   logging ("IRC command for stop bot")
	elif msg.payload=="start":
           logging ("IRC command for start bot")
           os.system("irsend SEND_ONCE deebot KEY_PLAY")
# more callbacks, etc
client = mqtt.Client("Stofzuiger")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER,1883,60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
