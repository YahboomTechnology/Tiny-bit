# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, pin8, sleep
import tinybit
import music

display.off()
tinybit.init_IR(pin8)
music.play('c')


while True:
    # print(hex(tinybit.get_IR(pin8)))
    value = tinybit.get_IR(pin8)
    value = value >> 8

    # default
    if value == -0x01:
        music.pitch(0)
    # long pressed
    elif value == 0xff:
        music.pitch(500)
    else:
        # off
        if value == 0x00:
            music.play('c')
        # up
        elif value == 0x80:
            music.play('c')
        # light
        elif value == 0x40:
            music.play('c')
        # left
        elif value == 0x20:
            music.play('c')
        # buzzer
        elif value == 0xa0:
            music.play('c')
        # right
        elif value == 0x60:
            music.play('c')
        # spinleft
        elif value == 0x10:
            music.play('c')
        # down
        elif value == 0x90:
            music.play('c')
        # spinright
        elif value == 0x50:
            music.play('c')
        # +
        elif value == 0x30:
            music.play('c')
        # number 0
        elif value == 0xb0:
            music.play('c')
        # -
        elif value == 0x70:
            music.play('c')
        # number 1
        elif value == 0x08:
            music.play('c')
        # number 2
        elif value == 0x88:
            music.play('c')
        # number 3
        elif value == 0x48:
            music.play('c')
        # number 4
        elif value == 0x28:
            music.play('c')
        # number 5
        elif value == 0xa8:
            music.play('c')
        # number 6
        elif value == 0x68:
            music.play('c')
        # number 7
        elif value == 0x18:
            music.play('c')
        # number 8
        elif value == 0x98:
            music.play('c')
        # number 9
        elif value == 0x58:
            music.play('c')
