# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, pin12
import tinybit
import random
import neopixel

np = neopixel.NeoPixel(pin12, 2)
np.clear()
tinybit.car_HeadRGB(0, 0, 0)
display.show(Image.HAPPY)

item = 0


while True:
    voice = tinybit.getVoicedata()
    if voice > 100:
        item = random.randint(1, 6)
        tinybit.car_HeadRGB(random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        np[0] = (red, green, blue)
        np[1] = (red, green, blue)
        np.show()

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
