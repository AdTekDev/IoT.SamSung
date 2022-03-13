
# https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/

# Connect and control Raspberry Pi motion detector PIR
# The pins on the PIR are labelled:

#     VCC to pin 2 (5V)
#     OUT to pin 16 (GPIO 23)
#     GND an pin 6 (ground)

import RPi.GPIO as GPIO
import time
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
 
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print "Finish..."
GPIO.cleanup()
