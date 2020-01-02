# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import sleep, display, Image, pin12
import tinybit
import music
import neopixel

np = neopixel.NeoPixel(pin12, 2)
np.clear()
tinybit.car_HeadRGB(0, 0, 0)


while True:
    distance = tinybit.ultrasonic()
    if distance < 20:
        sleep(10)
        distance = tinybit.ultrasonic()
        if distance < 20:
            tinybit.car_stop()
            display.show(Image.NO)
            tinybit.car_HeadRGB(255, 0, 0)
            tinybit.car_back(100)
            music.pitch(523)
            sleep(500)
            tinybit.car_spinright(100)
            music.pitch(0)
            sleep(500)
    else:
        tinybit.car_HeadRGB(0, 255, 0)
        tinybit.car_run(100)
        music.pitch(0)
        display.show(Image.ARROW_S)
