import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from adafruit_epd.il0373 import Adafruit_IL0373
from PIL import Image, ImageDraw, ImageFont


class Display:
    WHITE = (0xFF, 0xFF, 0xFF)


    BLACK = (0x00, 0x00, 0x00)
    RED = (0xFF, 0x00, 0x00)

    BORDER = 20
    FONTSIZE = 36
    BACKGROUND_COLOR = WHITE
    FOREGROUND_COLOR = WHITE
    TEXT_COLOR = BLACK
    current_text = "Loading..."

    font = ImageFont.truetype("assets/DejaVuSans.ttf", FONTSIZE)

    def __init__(self) -> None:
        self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.ecs = digitalio.DigitalInOut(board.CE0)
        self.dc = digitalio.DigitalInOut(board.D22)
        self.rst = digitalio.DigitalInOut(board.D27)
        self.busy = digitalio.DigitalInOut(board.D17)
        self.srcs = None
        self.display = Adafruit_IL0373(152, 152, self.spi, cs_pin=self.ecs, dc_pin=self.dc, sramcs_pin=self.srcs,
                                       rst_pin=self.rst, busy_pin=self.busy)

    def __draw(self, text):
        image = Image.new("RGB", (self.display.width, self.display.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.display.width,
                       self.display.height), fill=self.BACKGROUND_COLOR)

        (font_width, font_height) = self.font.getsize(text)

        draw.text(
            (self.display.width // 2 - font_width // 2,
             self.display.height // 2 - font_height // 2),
            text,
            font=self.font,
            fill=self.TEXT_COLOR,
        )
        self.display.fill(Adafruit_EPD.WHITE)
        self.display.image(image)
        self.display.display()
   
    def update_display(self, new_text):
        if new_text != self.current_text:
            self.current_text = new_text
            self.__draw(self.current_text)
