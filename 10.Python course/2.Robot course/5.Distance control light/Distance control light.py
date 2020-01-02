# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, pin12
import tinybit
import neopixel

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 2)
np.clear()
tinybit.car_HeadRGB(0, 0, 0)

while True:
    distance = tinybit.ultrasonic()
    if distance > 0 and distance <= 4:
        tinybit.car_HeadRGB(255, 0, 0)
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np.show()

    if distance > 4 and distance <= 8:
        tinybit.car_HeadRGB(0, 255, 0)
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np.show()

    if distance > 8 and distance <= 12:
        tinybit.car_HeadRGB(0, 0, 255)
        np[0] = (0, 0, 255)
        np[1] = (0, 0, 255)
        np.show()

    if distance > 12 and distance <= 16:
        tinybit.car_HeadRGB(255, 255, 0)
        np[0] = (255, 255, 0)
        np[1] = (255, 255, 0)
        np.show()

    if distance > 16 and distance <= 20:
        tinybit.car_HeadRGB(255, 255, 255)
        np[0] = (255, 255, 255)
        np[1] = (255, 255, 255)
        np.show()

    if distance > 20:
        tinybit.car_HeadRGB(0, 0, 0)
        np.clear()
