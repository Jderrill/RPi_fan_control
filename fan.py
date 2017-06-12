# -*- coding: utf-8 -*-
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

#GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,GPIO.LOW)

def CPUtemp():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp

def turnOnFan(temp):
##    temp = CPUtemp()
    high_temp = 50.0
    
    if temp > high_temp:
        GPIO.output(13,GPIO.HIGH)
        print temp
    else:
        GPIO.output(13,GPIO.LOW)
        print temp
        sleep(30)
    return()
    
    
while True:
##    temp = raw_input("temp")
    temp = float(CPUtemp())
##    print temp
    turnOnFan(temp)
