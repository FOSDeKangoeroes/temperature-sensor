import glob
import time

class TempSensorManager:
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    def __read_raw_temp(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def read_temp(self, device):
        lines = self.__read_raw_temp(device)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.__read_raw_temp(device)
        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def get_temp_sensor_files(self):
        return glob.glob(TempSensorManager.base_dir + '28*')

    def get_devices(self):
        sensors = self.get_temp_sensor_files()
        device_count = len(sensors)
        devices = []

        for i in range(device_count):
            devices.append(sensors[i] + '/w1_slave')

        return devices
        