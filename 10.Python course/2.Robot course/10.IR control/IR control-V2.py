# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
# from microbit import *
from microbit import display, sleep, pin8, pin12
import tinybit
import music
import neopixel

np = neopixel.NeoPixel(pin12, 2)
np.clear()
tinybit.car_HeadRGB(0, 0, 0)
tinybit.init_IR(pin8)
tinybit.car_stop()
display.off()

speed = 100
a = 0
music.play('c')


while True:
    # print(hex(tinybit.get_IR(pin8)))
    value = tinybit.get_IR(pin8)
    value = value >> 8

    # default
    if value == -0x01:
        a = a + 1
        if (a > 3):
            tinybit.car_stop()
            a = 0
    # long pressed
    elif value == 0xff:
        a = 0
    else:
        # off
        if value == 0x00:
            tinybit.car_HeadRGB(0, 0, 0)
        # up
        elif value == 0x80:
            tinybit.car_run(speed, speed)
        # light
        elif value == 0x40:
            tinybit.car_HeadRGB(255, 255, 255)
        # left
        elif value == 0x20:
            tinybit.car_left(speed)
        # buzzer
        elif value == 0xa0:
            music.pitch(698)
            sleep(400)
            music.stop()
        # right
        elif value == 0x60:
            tinybit.car_right(speed)
        # spinleft
        elif value == 0x10:
            tinybit.car_spinleft(speed, speed)
        # down
        elif value == 0x90:
            tinybit.car_back(speed, speed)
        # spinright
        elif value == 0x50:
            tinybit.car_spinright(speed, speed)
        # +
        elif value == 0x30:
            speed = speed + 40
            if speed > 255:
                speed = 255
                music.pitch(500)
                sleep(300)
                music.stop()
            else:
                music.pitch(226)
                sleep(300)
                music.stop()
        # number 0
        elif value == 0xb0:
            speed = 100
            music.pitch(226)
            sleep(300)
            music.stop()
        # -
        elif value == 0x70:
            speed = speed - 40
            if speed < 0:
                speed = 0
                music.pitch(60)
                sleep(300)
                music.stop()
            else:
                music.pitch(226)
                sleep(300)
                music.stop()
        # number 1
        elif value == 0x08:
            music.play('c')
        # number 2
        elif value == 0x88:
            music.play('d')
        # number 3
        elif value == 0x48:
            music.play('e')
        # number 4
        elif value == 0x28:
            music.play('f')
        # number 5
        elif value == 0xa8:
            music.play('g')
        # number 6
        elif value == 0x68:
            music.play('a')
        # number 7
        elif value == 0x18:
            music.play('b')
        # number 8
        elif value == 0x98:
            np[0] = (255, 255, 255)
            np[1] = (255, 255, 255)
            np.show()
        # number 9
        elif value == 0x58:
            np.clear()
