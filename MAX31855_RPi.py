# 
# This file was edited from www.github.com/engineertype/MAX31855/MAX31855_RPi.txt
# Edits include updated libraries, a different GPIO layout, and data storage.
# Josh Carlile, Hydroside Systems, 2021
# 

import time
from datetime import datetime

import board
import gpiozero as gpio
import adafruit_max31855
import RPi.GPIO as GPIO

import data_storage as data


# Define a function to convert celsius to fahrenheit.
def c_to_f(temp_c):
    return temp_c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration (using GPIO pin names)
SCLK = 11
CS = 8
MOSI = 10
MISO = 9

spi = board.SPI()
sensor = adafruit_max31855.MAX31855(spi, GPIO.setup(CS, GPIO.OUT))


# thermocouple selector pins (using BOARD pin names)
T0 = 17 # GPIO17
T1 = 27 # 
T2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(T0, GPIO.OUT)
GPIO.setup(T1, GPIO.OUT)
GPIO.setup(T2, GPIO.OUT)

# Loop printing measurements every second.
print('Press Ctrl-C to quit.')

thermocouple = 0 # Which channel am I referencing?
current_data = []

while True:
    # bitwise operators select which thermocouple is to be referenced -- start at 0!
    GPIO.output(T0, tc & 1<<0)
    GPIO.output(T1, tc & 1<<1)
    GPIO.output(T2, tc & 1<<2)

    time.sleep(0.125)
    temp = sensor.temperature()
    internal = sensor.reference_temperature()

    # print('Sensor', tc)
    # print('{1:0.3F}'.format(temp, c_to_f(temp)))

    # print('Thermocouple Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp, c_to_f(temp)))
    # print(' Internal Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal, c_to_f(internal)))

    # TODO: Plot at the end of each cycle

    # if this is not the last thermocouple, add the data and move to next
    if tc < 3:
        current_data.append(temp)
        tc += 1
    else:
        current_data.append(temp.__str__())
        current_data.append(datetime.now().__str__())

    tc = tc + 1 if tc < 3 else 0 # Adds one on tc = 0, 1, 2, and resets to 0 when tc = 3