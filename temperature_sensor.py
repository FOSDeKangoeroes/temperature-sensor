import sys
from RPi import GPIO
from temp_sensor_manager import TempSensorManager
from threading import Thread
import time
from lcd import LCD
from led import LED

temp_manager = TempSensorManager()
lcd = LCD()
led = LED()

sensors = temp_manager.get_temp_sensor_files()

lcd_thread = Thread(target = lcd.run)
lcd_thread.start()

try:
    while True:
        allTemps = list()
        for device in temp_manager.get_devices():
            temp = temp_manager.read_temp(device)
            allTemps.append((device, temp))
        meanTemp = temp_manager.get_average_from_sensors()
        lcd.set_display_value("{0:.2f}".format(meanTemp))
        led.update_led(meanTemp)
        print(allTemps)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
