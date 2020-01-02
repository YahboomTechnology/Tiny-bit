# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import tinybit
import radio

display.show(Image.HEART)
radio.on()
radio.config(group=1)


while True:
    incoming = radio.receive()
    if incoming == 'up':
        tinybit.car_run(100, 100)
    elif incoming == 'down':
        tinybit.car_back(100, 100)
    elif incoming == 'left':
        tinybit.car_spinleft(100, 100)
    elif incoming == 'right':
        tinybit.car_spinright(100, 100)
    elif incoming == 'stop':
        tinybit.car_stop()

    if incoming == 'R':
        tinybit.car_HeadRGB(255, 0, 0)
    elif incoming == 'G':
        tinybit.car_HeadRGB(0, 255, 0)
    elif incoming == 'B':
        tinybit.car_HeadRGB(0, 0, 255)
    elif incoming == 'Y':
        tinybit.car_HeadRGB(255, 255, 0)
    elif incoming == 'turn_off':
        tinybit.car_HeadRGB(0, 0, 0)
