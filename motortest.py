# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:49:55 2018

@author: Gerard
"""

import RPi.GPIO as GPIO
import time
print("Program starting!")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
GPIO.cleanup()