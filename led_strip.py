import threading
import board
import neopixel
import time
from utils import calculate_color_for_breathe

class LedStrip:

    current_color = (0, 0, 0)
    running = True

    def __init__(self, num_pixels, pin) -> None:
        self.num_pixels = num_pixels
        self.pixel_pin = pin
        self.order = neopixel.GRB
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin,
            self.num_pixels,
            brightness=1,
            auto_write=False,
            pixel_order=self.order
            )

    def breathe(self, rgb):
        (red, green, blue) = rgb
        for i in range (100,225,1):
            r = calculate_color_for_breathe(i, red)
            g = calculate_color_for_breathe(i, green)
            b = calculate_color_for_breathe(i, blue)
            self.pixels.fill((r,g,b))
            self.pixels.show()
            time.sleep(0.01)

        for i in range(225,100,-1):
            r = calculate_color_for_breathe(i, red)
            g = calculate_color_for_breathe(i, green)
            b = calculate_color_for_breathe(i, blue)
            self.pixels.fill((r,g,b))
            self.pixels.show()
            time.sleep(0.01)

    def turn_off(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
        time.sleep(1)

    def run(self):
        t = threading.currentThread()
        while getattr(t, "running", True):
            self.breathe(self.current_color)
        print('turning off')
        self.turn_off()
