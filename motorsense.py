# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 00:01:50 2018

@author: Gerard
"""
from __future__ import division
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_PCA9685
import time
import math

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

defpos = mcp.read_adc(0)
print(defpos)
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

print('Reading MCP3008 values, press Ctrl-C to quit...')
while True:
    val = roundup(mcp.read_adc(0))
    servoinp = defpos - val
    print(val)
    print(roundup(val))
    print(roundup(roundup(val) / 30 * 15))
    print("+=-=-=-=-=-=-=-=-=-=-=-=-=-=+")
    pwm.set_pwm(15, 0,roundup(roundup(val) / 30 * 14))
    #print(val)
    #print(servoinp)
    #print("-=+=+=+=+=+=+=+=+=+=-")
    #pwm.set_pwm(15, 0, servoinp)
    time.sleep(0.3)
