# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep
import tinybit

display.show(Image.HAPPY)


while True:
    tinybit.car_run(0, 0)
    sleep(1000)
    tinybit.car_run(50, 50)
    sleep(1000)
    tinybit.car_run(100, 100)
    sleep(1000)
    tinybit.car_run(150, 100)
    sleep(1000)
    tinybit.car_run(200, 200)
    sleep(1000)
    tinybit.car_run(255, 255)
    sleep(1000)
