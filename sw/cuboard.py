# v1.2

import time
import machine
import neopixel

NEOPIXEL_PIN = 5
MOTOR_PIN = 4
STEPPER1_PIN = 14
STEPPER2_PIN = 12
STEPPER3_PIN = 13
STEPPER4_PIN = 15
WHITE = (255, 255, 180)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def fillfour(value, np1,np2,np3,np4):
    np1.fill(value);np1.write()
    np2.fill(value);np2.write()
    np3.fill(value);np3.write()
    np4.fill(value);np4.write()

def fill(value, np):
    np.fill(value);np.write()

def filltwo(value, np1,np2):
    np1.fill(value);np1.write()
    np2.fill(value);np2.write()
        

def readAndAdjust(adc,threshhold, margin):
    t = threshhold
    while True:
        value = adc.read()
        oldValue = value
        # Wait until a detection was made
        if value <= 1024:
            
            # Movement detected
            # Check again for threshhold changes
            time.sleep(0.4)
            value = adc.read()

            # still smaller
            if value <= t * margin: 
                print(f"--> Lowered threshold from {t} to {value}")
                t = value # Update threshold but continue reading
            else:
                # If the threshoold was not exeeded it's a detection
                # Use the second reading as the new threshhold
                # The old value was not repeated
                return (oldValue, value)
        elif value > t / margin:
            time.sleep(0.4)
            value = adc.read()
            # still bigger
            if value > t / margin:
                print(f"++> Raised threshold from {t} to {value}")
                t = value # Update threshold but continue reading 
            
 
