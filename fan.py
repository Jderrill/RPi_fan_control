# -*- coding: utf-8 -*-
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.LOW)

def CPUtemp():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp

def turnOnFan(temp):
    high_temp = 50.0
    
    if temp > high_temp:
        GPIO.output(13,GPIO.HIGH)
    else:
        GPIO.output(13,GPIO.LOW)
        sleep(30)
    return()
    
    
while True:
    temp = float(CPUtemp())
    turnOnFan(temp)
