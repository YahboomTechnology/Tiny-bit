from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 2)
while True:
    for pixel_id in range(0, len(np)):
        np[0] = (255, 0, 0)
        np.show()
        sleep(200)
        np.clear()
        np[1] = (0, 255, 0)
        np.show()
        sleep(200)
        np.clear()