# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import tinybit
from random import randint

display.show(Image.HAPPY)
item = 0


while True:
    voice = tinybit.getVoicedata()
    if voice > 100:
        item = randint(1, 6)

    if item == 1:
        display.show(Image.HEART)
    elif item == 2:
        display.show(Image.COW)
    elif item == 3:
        display.show(Image.DUCK)
    elif item == 4:
        display.show(Image.TARGET)
    elif item == 5:
        display.show(Image.SNAKE)
    elif item == 6:
        display.show(Image.GIRAFFE)
