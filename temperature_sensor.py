import sys
import time
from RPi import GPIO
from temp_sensor_manager import TempSensorManager
from threading import Thread
from lcd import LCD
from led import LED

temp_manager = TempSensorManager()
lcd = LCD()
led = LED()

sensors = temp_manager.get_temp_sensor_files()

lcd_thread = Thread(target = lcd.run)
lcd_thread.start()

devices = temp_manager.get_devices()

try:
    while True:
        allTemps = list()
        for device in devices:
            temp = temp_manager.read_temp(device)
            allTemps.append((device, temp))
        meanTemp = temp_manager.get_average_from_sensors()
        lcd.set_display_value("{0:.2f}".format(meanTemp))
        led.update_led(meanTemp)
        time.sleep(30)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
