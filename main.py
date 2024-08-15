"""
ST7789 example for DC32 badge
"""
import st7789
import tft_config
from machine import Pin
import neopixel
import time


num_pixels = 9
np = neopixel.NeoPixel(machine.Pin(4), num_pixels)
tft = tft_config.config(3, buffer_size=4096) #rotation 3 for normal orientation, 1 for upside down

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            np[i] = wheel(rc_index & 255)
        np.write()
        time.sleep(0.01)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)



def demo(np):
    n = np.n

    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

def main():

    # Initial colors

    np[0] = (255, 0, 0)
    np[1] = (0, 128, 0)
    np[2] = (0, 0, 64)
    np[3] = (255, 0, 0)
    np[4] = (0, 128, 0)
    np[5] = (0, 0, 64)
    np[6] = (255, 0, 0)
    np[7] = (0, 128, 0)
    np[8] = (0, 0, 64)

    np.write()

    png_file_name = f'lhc-320x240.png'
    tft.init()
    print(f'Displaying {png_file_name}')
    tft.png(png_file_name, 0, 0)

    while(True):
        rainbow_cycle(0)  # Increase the number to slow down the rainbow

main()
