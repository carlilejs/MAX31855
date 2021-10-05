# Provided by a helpful customer - thanks!
#
# Here is the code written in python tested and working with the device on raspberry pi. You can adjust the sleep time as you want but you cannot go any lower than .125 ms from my experience.
#


import time

# import Adafruit_GPIO.SPI as SPI                 # TODO: change to spidev
# import Adafruit_MAX31855.MAX31855 as MAX31855   # TODO: change to 
# import RPi.GPIO as GPIO                         # TODO: change to gpiozero

import board
from digitalio import DigitalInOut, Direction
import adafruit_max31855


# Define a function to convert celsius to fahrenheit.
def c_to_f(temp_c):
    return temp_c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK = 25
CS = 24
DO = 18

spi = board.SPI()
sensor = adafruit_max31855.MAX31855(spi, digitalio.DigitalInOut(CS))


# thermocouple selector pins
T0 = 17
T1 = 27
T2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(T0, GPIO.OUT)
GPIO.setup(T1, GPIO.OUT)
GPIO.setup(T2, GPIO.OUT)

# Loop printing measurements every second.
print('Press Ctrl-C to quit.')

thermocouple = 0 # Which channel am I referencing?

while True:
    # bitwise operators select which 
    GPIO.output(T0, tc & 1<<0)
    GPIO.output(T1, tc & 1<<1)
    GPIO.output(T2, tc & 1<<2)

    time.sleep(0.125)
    temp = sensor.temperature()
    internal = sensor.reference_temperature()

    print('Sensor', tc)
    print('{1:0.3F}'.format(temp, c_to_f(temp)))

    #print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
    #print(' Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal)))
    
    tc = tc + 1 if tc < 3 else 0 # Adds one on tc = 0, 1, 2, and resets to 0 when tc = 3