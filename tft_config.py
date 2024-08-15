"""DC32 Badge display config"""

from machine import Pin, SoftSPI
from time import sleep
import st7789

TFA = 40	# top free area when scrolling
BFA = 40	# bottom free area when scrolling

def config(rotation=0, buffer_size=0, options=0):
    spi = SoftSPI(baudrate=62500000,
        polarity=0,
        phase=0,
        sck=Pin(8),
        mosi=Pin(6),
        miso=Pin(28)) #SoftSPI needs a MISO pin, used one of the gpio on the SAO

    return st7789.ST7789(
        spi,
        240,
        320,
        cs=Pin(9, Pin.OUT),
        dc=Pin(5, Pin.OUT),
        backlight=Pin(10, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
        color_order=st7789.RGB,
        inversion=False)
