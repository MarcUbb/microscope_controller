from machine import SPI, Pin
from xpt2046 import Touch
from time import sleep

def test(x,y):
    print(x,y)

spi = SPI(1, baudrate=1000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

xpt = Touch(spi=spi, cs=Pin(5), int_pin=Pin(0), int_handler=test)

while True:
    print(xpt.raw_touch())
    sleep(0.1)

