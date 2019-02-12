# Python Script To Control Garage Door
 
# Load libraries
import RPi.GPIO as GPIO
import time
from bottle import route, run, template

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)

# Handle http requests to the root address
@route('/')
def index():
 return 'Go away.'

# Handle http requests to /garagedoor
@route('/pomp/:gpio_num')
def pomp(gpio_num=0):
 if gpio_num == '0':
  return 'Nothing specified'

 elif gpio_num == 'start':
  GPIO.output(7, False)
  time.sleep(.8)
  GPIO.output(7, True)
  return 'pomp gestart.'
 elif gpio_num == 'stop':
  GPIO.output(7, True)
  return 'pomp gestopt.'



run(host='0.0.0.0', port=1234)
