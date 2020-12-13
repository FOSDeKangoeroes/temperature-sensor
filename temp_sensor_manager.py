import glob

class TempSensorManager:
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave' 

    def __read_raw_temp(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return lines
    
    def read_temp(self):
        lines = self.__read_raw_temp(TempSensorManager.device_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.__read_raw_temp(TempSensorManager.device_file)
        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
    
    def get_temp_sensor_files(self):
        return glob.glob(TempSensorManager.base_dir + '28*')