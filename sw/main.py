import machine
adc = machine.ADC(0)
import time
from machine import Pin

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION
from machine import Pin

import cuboard
from cuboard import readAndAdjust
stepper = Stepper(HALF_STEP, Pin(14, Pin.OUT), Pin(12, Pin.OUT), Pin(5, Pin.OUT), Pin(10, Pin.OUT), delay=.003 )  

ROTATIONS = 4
MARGIN = 0.9

# photoresistor to 5V  
# 10kOhm resistor to GND
def sensorDetected(value):
    global stepper, FULL_ROTATION, ROTATIONS
    print("sensor detected with value " + str(value))
    stepper.step(FULL_ROTATION * ROTATIONS, -1)
    

print("Starting reading ...")
threshhold = adc.read()
print("First value = " + str(threshhold))

while True:
    (value, threshhold) = readAndAdjust(adc, threshhold, MARGIN)
    sensorDetected(value)
    time.sleep(.01)
