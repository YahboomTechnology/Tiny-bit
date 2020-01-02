# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep
import tinybit


while True:
    tinybit.car_run(150)
    display.show(Image.ARROW_S)
    sleep(1000)
    tinybit.car_back(150)
    display.show(Image.ARROW_N)
    sleep(1000)
    tinybit.car_left(150)
    display.show(Image.ARROW_E)
    sleep(1000)
    tinybit.car_right(150)
    display.show(Image.ARROW_W)
    sleep(1000)
    tinybit.car_spinleft(150)
    display.show(Image.ARROW_E)
    sleep(1000)
    tinybit.car_spinright(150)
    display.show(Image.ARROW_W)
    sleep(1000)
    tinybit.car_stop()
    display.clear()
    sleep(1000)
