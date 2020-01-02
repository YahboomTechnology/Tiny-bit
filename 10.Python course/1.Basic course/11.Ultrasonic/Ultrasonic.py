# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import tinybit

display.show(Image.HAPPY)


while True:
    a = tinybit.ultrasonic()
    print(a)
