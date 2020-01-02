# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import sleep, display, Image, button_a, button_b
import tinybit

display.show(Image.HAPPY)
show_L = Image("90000:90000:90000:90000:99999")
show_O = Image("09990:90009:90009:90009:09990")
show_D = Image("99000:90900:90090:90009:99999")
show_Z = Image("99999:00090:00900:09000:99999")

a = 0
b = 0

speed_run = 100
speed_spin = 80

def run_L():
    display.show(show_L)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_spinleft(speed_spin)
        sleep(400)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_stop()
        global b
        b = 0

def run_O():
    display.show(show_O)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_spinleft(speed_spin)
        sleep(400)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_spinleft(speed_spin)
        sleep(400)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_spinleft(speed_spin)
        sleep(400)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_stop()
        global b
        b = 0

def run_D():
    display.show(show_D)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_spinleft(speed_spin)
        sleep(500)
        tinybit.car_run(speed_run)
        sleep(1500)
        tinybit.car_spinleft(speed_spin)
        sleep(500)
        tinybit.car_run(speed_run)
        sleep(1200)
        tinybit.car_stop()
        global b
        b = 0

def run_Z():
    display.show(show_Z)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_run(speed_run)
        sleep(1000)
        tinybit.car_spinright(speed_spin)
        sleep(500)
        tinybit.car_run(speed_run)
        sleep(1300)
        tinybit.car_spinleft(speed_spin)
        sleep(600)
        tinybit.car_run(speed_run)
        sleep(1300)
        tinybit.car_stop()
        global b
        b = 0


while True:
    if button_a.was_pressed():
        a = a + 1
        if a >= 5:
            a = 1
    if button_b.was_pressed():
        b = 1
    if a == 1:
        run_L()
    elif a == 2:
        run_O()
    elif a == 3:
        run_D()
    elif a == 4:
        run_Z()
