# Python Script To Control GPIO

# Load libraries
import RPi.GPIO as GPIO
import time
import random
# Set up the GPIO pins
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)

#KEEP this scipt running
#nohup python /home/pismurf/mqqt//mqqt/deebot_subscriber.py &


#op de windows machine een environ omgeving ingesteld, om dev /test/ staging te faciliteren
#environment[CODE_env]="dev"

import os
import paho.mqtt.client as mqtt

#should be environment settings!
#MQTT_SERVER = "77.248.61.13"
MQTT_SERVER = "192.168.0.60"

#Subscription paths
MQTT_PATH = "pomp"


def on_connect(client, userdata, flags, rc):
	print("Pomp Subscribed (code "+str(rc)+")")
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+msg.payload)
	if msg.payload=="stop":
		print ("Stopping the pomp")
		#sending GPIO command
		GPIO.output(7, True)
	elif msg.payload=="start":
		print ("Starting the pomp")
		#sending GPIO command
		GPIO.output(7, False)
		time.sleep(.8)
		GPIO.output(7, True)
# more callbacks, etc
client = mqtt.Client("Waterpomp")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER,1883,60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
