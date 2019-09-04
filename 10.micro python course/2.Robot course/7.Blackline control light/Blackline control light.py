# Shenzhen Yahboom Technology Co., Ltd.
# modified from Dolphin
# Tiny-bit  2109,07,23

from microbit import *

import neopixel
np = neopixel.NeoPixel(pin12, 2)
# Two RGB light of Tiny-bit connect to Pin 12 of micro:bit

Val1 = pin13.read_digital()
pin13.set_pull(pin13.NO_PULL)
Val2 = pin14.read_digital()
pin14.set_pull(pin13.NO_PULL)
# Because Pin Pin13 and Pin14 micro:bit internal default is PULL_DOWN state,
# On the hardware, Pin13 and Pin14 are connected to a pull-up resistor,
# and there will be conflicts between the them.
# So we need to set this two pin to ON_PULL in the program
# (which is pull up nor pull down)
# Calling set_pull will configure the pin to be in read_digital mode

while True:
    if pin13.read_digital() == 1 and pin14.read_digital() == 1:
        # Two tracking sonser connect Pin13,Pin14 of micro:bit
        np[0] = (255, 255, 0)  # Yellow light
        np[1] = (255, 255, 0)  # Yellow light
        np.show()
        display.show(Image.ARROW_S)
    elif pin13.read_digital() == 1 and pin14.read_digital() == 0:
        np[0] = (255, 255, 0)  # Yellow light
        np[1] = (255, 0, 255)  # Purple light
        np.show()
        display.show(Image.ARROW_E)
    elif pin13.read_digital() == 0 and pin14.read_digital() == 1:
        np[0] = (255, 0, 255)  # Purple light
        np[1] = (255, 255, 0)  # Yellow light
        np.show()
        display.show(Image.ARROW_W)
    else:
        np[0] = (255, 0, 255)  # Purple light
        np[1] = (255, 0, 255)  # Purple light
        np.show()
        display.show(Image.HEART)