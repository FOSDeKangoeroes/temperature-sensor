import statistics
from threading import Thread
from datetime import datetime
import time
import board

from RPi import GPIO
from temp_sensor_manager import TempSensorManager
from csv_logger import CsvLogger
from utils import get_temperature_color
from led_strip import LedStrip

def format_reading(device_name, reading_value):
    current_date = datetime.now().isoformat()
    return [current_date, device_name, reading_value]

try:
    LOG_FILE = '/home/pi/log.csv'

    temp_manager = TempSensorManager()
    ledStrip = LedStrip(10, board.D18)
    csv_logger = CsvLogger(LOG_FILE)

    sensors = temp_manager.get_temp_sensor_files()

    led_strip_thread = Thread(target=ledStrip.run)
    led_strip_thread.start()

    devices = temp_manager.get_devices()

    while True:
        all_temps = list()
        for device in devices:
            temp = temp_manager.read_temp(device)
            all_temps.append((device, temp))
            csv_logger.write_reading(format_reading(device, temp))
        mean_temp = statistics.mean(all_temps)
        print(all_temps)
        ledStrip.current_color = get_temperature_color(mean_temp)
        time.sleep(180)
except KeyboardInterrupt:
    led_strip_thread.running = False
    led_strip_thread.join()
    GPIO.cleanup()
