# Python Script To Control Garage Door

# Load libraries
import RPi.GPIO as GPIO
import time
from bottle import route, run, template

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(7, True)   
GPIO.output(11, True)

# Handle http requests to the root address
@route('/')
def index():
 return 'Go away.'

# Handle http requests to /garagedoor
@route('/garagedoor/:doornum')
def garagedoor(doornum=0):
 if doornum == '0':
 return 'No door number specified'

 elif doornum == '1':
 GPIO.output(7, False)
 time.sleep(.8)
 GPIO.output(7, True)
 return 'Door number 1 cycled.'

 elif doornum == '2':
 GPIO.output(11, False)
 time.sleep(.8)
 GPIO.output(11, True)

 return 'Door number 2 cycled'

run(host='0.0.0.0', port=1234)
