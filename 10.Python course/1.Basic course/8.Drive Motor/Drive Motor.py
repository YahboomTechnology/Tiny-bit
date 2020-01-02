# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import tinybit

display.show(Image.HAPPY)
tinybit.setMotorPWM(255, 255, 1000)
tinybit.setMotorPWM(0, 0, 1000)
tinybit.setMotorPWM(-255, -255, 1000)
tinybit.setMotorPWM(0, 0, 1000)
