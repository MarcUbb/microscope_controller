"""Search online for pwned passwords."""
from machine import Pin, SPI
from xpt2046 import Touch
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from time import sleep


class PwnLookup(object):
    """Checks if password is pwned."""

    def __init__(self, spi1, spi2, dc=4, cs1=16, rst=17, cs2=5, rotation=270):
        """Initialize PwnLookup."""
        # Set up display
        self.display = Display(spi1, dc=Pin(dc), cs=Pin(cs1), rst=Pin(rst),
                               width=320, height=240, rotation=rotation)

        # Load font
        #self.unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)

        # Set up Keyboard
        #self.keyboard = TouchKeyboard(self.display, self.unispace)

        # Set up touchscreen
        self.xpt = Touch(spi2, cs=Pin(cs2), int_pin=Pin(0),
                         int_handler=self.touchscreen_press)
        #self.wlan = WLAN(STA_IF)

    

    def touchscreen_press(self, x, y):
        print("bruh")


def main():
    """Start PwnLookup."""
    spi1 = SPI(1, baudrate=51200000,
               sck=Pin(14), mosi=Pin(13), miso=Pin(12))
    spi2 = SPI(2, baudrate=1000000,
               sck=Pin(18), mosi=Pin(23), miso=Pin(19))

    PwnLookup(spi1, spi2)

    while True:
        sleep(.1)


main()
