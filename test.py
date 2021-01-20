# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:35:04 2018

@author: Gerard
"""
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
i = 0
try:
    while True:
        i += 1
        print ("Cycle Number 1, loop " + str(i))
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
        print ("Cycle Number 2, loop " + str(i))
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
        print ("Cycle Number 3, loop " + str(i))
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
except KeyboardInterrupt:
    print (" ")
    print ("~-=-=-=-=++=-=-=-=-~")
    print ("Program ended. Finished on loop " + str(i))
    GPIO.cleanup()