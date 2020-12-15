import os
import sys
import glob
import time
from threading import Thread
import RPi.GPIO as GPIO
import lcd

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

BASE_DIR = '/sys/bus/w1/devices/'
device_folder = glob.glob(BASE_DIR + '28*')[0]
device_file = device_folder + '/w1_slave'

PIN_RED = 26
PIN_GREEN = 19
PIN_BLUE = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)

def read_temp_raw():
    file = open(device_file, 'r')
    lines = file.readlines()
    file.close()
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

def blink_led(value):
    if value < 25:
        GPIO.output(PIN_GREEN, 0)
        GPIO.output(PIN_RED, 0)
        GPIO.output(PIN_BLUE, 1)
    elif  value >= 25 and value < 27:
        GPIO.output(PIN_BLUE, 0)
        GPIO.output(PIN_RED, 0)
        GPIO.output(PIN_GREEN, 1)
    else:
        GPIO.output(PIN_BLUE, 0)
        GPIO.output(PIN_GREEN, 0)
        GPIO.output(PIN_RED, 1)


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
