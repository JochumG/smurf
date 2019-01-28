from flask import Flask
import uwsgi

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey I'm using Docker AND MQQT! Az well"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)



#import paho.mqtt.publish as publish
#MQTT_SERVER = "192.168.0.60"
#MQTT_PATH = "sensordata"
#publish.single(MQTT_PATH, "Hello publish local MQTTT!", hostname=MQTT_SERVER)
print("Stopped...")
