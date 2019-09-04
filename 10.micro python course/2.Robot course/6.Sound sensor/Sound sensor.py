# Shenzhen Yahboom Technology Co., Ltd.
# modified from Dolphin
# Tiny-bit  2109,07,23

from microbit import *

horn = Image("00090:"
             "90990:"
             "99990:"
             "90990:"
             "00090")

calibration_Val = pin1.read_analog()
sleep(500)

while True:
    Voice_Val = pin1.read_analog()
    if Voice_Val > calibration_Val + 50:
        # Detected changes in the external environment of the
        # current environment,
        # this parameter can be changed by yourself
        display.show(horn)
        sleep(200)
    else:
        display.show(Image.HAPPY)