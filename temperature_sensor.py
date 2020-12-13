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
    temp = temp_manager.read_temp()
    print(temp)
    time.sleep(1)

def device_names:
    names = list()

    for i in range(device_count):
        names.append(devices[i])
        temp = names[i][20:35]
        names[i] = temp
    return names