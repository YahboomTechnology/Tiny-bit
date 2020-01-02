# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep
import tinybit

display.show(Image.HAPPY)

while True:
    tinybit.car_HeadRGB(255, 0, 0)
    sleep(500)
    tinybit.car_HeadRGB(0, 255, 0)
    sleep(500)
    tinybit.car_HeadRGB(0, 0, 255)
    sleep(500)
    tinybit.car_HeadRGB(255, 255, 255)
    sleep(500)
    tinybit.car_HeadRGB(0, 0, 0)
    sleep(500)
