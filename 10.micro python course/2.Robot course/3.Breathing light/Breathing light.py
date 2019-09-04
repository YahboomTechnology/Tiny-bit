from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 2)
# Two RGB light of Tiny-bit connect to Pin 12 of micro:bit

while True:
    for num1 in range(255, 0, -1):    # From 255 to 0, increase by -1 each time
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (num1, 0, num1)    # purple
            np.show()
            sleep(5)
            # RGB lights are changed gradually from light to dark
    for num1 in range(0, 255, 1):    # From 0 to 255, increase by 1 each time
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (num1, 0, num1)   # purple
            np.show()
            sleep(5)
            # RGB lights are changed gradually from dark to light