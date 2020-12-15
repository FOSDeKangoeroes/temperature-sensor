from temp_sensor_manager import TempSensorManager
import time

temp_manager = TempSensorManager()

sensors = temp_manager.get_temp_sensor_files()

while True:
    allTemps = list()
    for device in temp_manager.get_devices():
        temp = temp_manager.read_temp(device)
        allTemps.append((device, temp))

    print(allTemps)
    time.sleep(1)
