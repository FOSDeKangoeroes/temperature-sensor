import os
import sys
import glob
import time
import RPi.GPIO as GPIO
import lcd
from threading import Thread
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

pinRed = 26
pinGreen = 19
pinBlue = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pinRed, GPIO.OUT)
GPIO.setup(pinGreen, GPIO.OUT)
GPIO.setup(pinBlue, GPIO.OUT)
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        # time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_c = round(temp_c, 2)
        return temp_c

def blink_led(temp):
    if temp < 25:
        GPIO.output(pinGreen, 0)
        GPIO.output(pinRed, 0)
        GPIO.output(pinBlue, 1)
    elif  temp >= 25 and temp < 27:
        GPIO.output(pinBlue, 0)
        GPIO.output(pinRed, 0)
        GPIO.output(pinGreen, 1)
    else:
        GPIO.output(pinBlue, 0)
        GPIO.output(pinGreen, 0)
        GPIO.output(pinRed, 1)


thread = Thread(target = lcd.run)
thread.start()

try:	
  while True:
    temp = read_temp()
    blink_led(temp)
    lcd.toDisplay = "{0:.2f}".format(temp)
    time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()