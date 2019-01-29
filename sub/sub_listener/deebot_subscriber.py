#Eerste deepbot actie script listener 28-01-3019
#KEEP this scipt running
#nohup python /home/pismurf/mqqt//mqqt/deebot_subscriber.py &

#https://www.instructables.com/id/How-To-Useemulate-remotes-with-Arduino-and-Raspber/
#een deebot lirc file maken
#https://raspberrypi.stackexchange.com/questions/81876/raspberry-pi-3-not-lirc-not-running-working

#deebot.lircd.conf
#sudo irrecord -d /dev/lirc0 ~/lircd.conf
import os
       

import paho.mqtt.client as mqtt

MQTT_SERVER = "77.248.61.13"
MQTT_PATH = "deebot"

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Deebot Connected (code "+str(rc)+")")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    print("Subcribing to be able to start Deebot")
    client.subscribe(MQTT_PATH)

    
	
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+msg.payload)
	if msg.payload=="stop":
	   print ("IRC command for stop bot")
	   #sending IRC command
	   os.system("irsend SEND_ONCE deebot KEY_STOP")

	   
	elif msg.payload=="start":
         print ("IRC command for start bot")
         os.system("irsend SEND_ONCE deebot KEY_PLAY")

	# more callbacks, etc
client = mqtt.Client("script")
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER,1883,60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
