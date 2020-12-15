import RPi._GPIO as GPIO

class LED:
    PIN_RED = 26
    PIN_GREEN = 16
    PIN_BLUE = 13

    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_RED, GPIO.OUT)
        GPIO.setup(self.PIN_GREEN, GPIO.OUT)
        GPIO.setup(self.PIN_BLUE, GPIO.OUT)

    def update_led(self, current_temp):
        if current_temp < 25:
            GPIO.output(self.PIN_GREEN, 0)
            GPIO.output(self.PIN_RED, 0)
            GPIO.output(self.PIN_BLUE, 1)
        elif current_temp >= 25 and current_temp < 27:
            GPIO.output(self.PIN_BLUE, 0)
            GPIO.output(self.PIN_RED, 0)
            GPIO.output(self.PIN_GREEN, 1)
        else:
            GPIO.output(self.PIN_BLUE, 0)
            GPIO.output(self.PIN_GREEN, 0)
            GPIO.output(self.PIN_RED, 1)
