# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:43:36 2018

@author: Gerard
"""

import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)
"""
pwm.set_pwm(15, 0, 600)
time.sleep(3)
pwm.set_pwm(15, 0, 0)
"""
x = 0
y = 600 #this is the maximum position
interval = 6
while x != y:
    pwm.set_pwm(15, 0, x)
    print(x)
    time.sleep(0.05) #A good update speed
    x += interval

if x == y:
    pwm.set_pwm(15, 0, 0)
    print("end")