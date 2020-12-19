import csv

class CsvLogger:

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def write_reading(self, reading):
        with open(self.file_path, mode= 'a') as readings_file:
            writer = csv.writer(
                readings_file,
                delimiter= ';',
                quotechar= '"',
                quoting =  csv.QUOTE_MINIMAL
                )
            writer.writerow(reading)
