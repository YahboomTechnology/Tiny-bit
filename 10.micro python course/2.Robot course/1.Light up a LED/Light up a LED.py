from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 2)  # RGB light connects to micro:bit's P12 pin
while True:
    for pixel_id in range(0, len(np)):
        np[0] = (255, 0, 0)   # red
        np.show()  # Show
        sleep(200)
