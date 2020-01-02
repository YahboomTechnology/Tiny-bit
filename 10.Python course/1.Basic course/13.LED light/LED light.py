# Write your code here :-)
from microbit import *
import neopixel
import random

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 2)


while True:

    for pixel_id in range(0, len(np)):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        np.clear()
        np[pixel_id] = (R, G, B)
        np.show()
        sleep(500)
