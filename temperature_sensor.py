import sys
import time
from threading import Thread
from datetime import datetime
from RPi import GPIO
from temp_sensor_manager import TempSensorManager
from lcd import LCD
from led import LED
from csv_logger import CsvLogger

def format_reading(device_name, reading_value):
    current_date = datetime.now().isoformat()
    return [current_date, device_name, reading_value]

try:
    LOG_FILE = '/home/pi/log.csv'

    temp_manager = TempSensorManager()
    lcd = LCD()
    led = LED()
    csv_logger = CsvLogger(LOG_FILE)

    sensors = temp_manager.get_temp_sensor_files()

    lcd_thread = Thread(target=lcd.run)
    lcd_thread.start()

    devices = temp_manager.get_devices()

    while True:
        allTemps = list()
        for device in devices:
            temp = temp_manager.read_temp(device)
            allTemps.append((device, temp))
            csv_logger.write_reading(format_reading(device, temp))
        meanTemp = temp_manager.get_average_from_sensors()
        print(allTemps)
        lcd.set_display_value("{0:.2f}".format(meanTemp))
        led.update_led(meanTemp)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
