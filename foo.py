# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:26:44 2018

@author: Gerard
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(12,GPIO.LOW)
time.sleep(0.5)
GPIO.output(12,GPIO.HIGH)


GPIO.cleanup()