from temp_sensor_manager import TempSensorManager
import time

temp_manager = TempSensorManager()

sensors = temp_manager.get_temp_sensor_files()

device_count = len(sensors)
devices = list()
i = 0

while i < device_count:
    devices.append(sensors[i] + '/w1_slave')
    i = i + 1


while True:
    allTemps = list()
    for device in devices:
        temp = temp_manager.read_temp(device)
        allTemps.append((device, temp))
     
    print(allTemps)
    time.sleep(1)

