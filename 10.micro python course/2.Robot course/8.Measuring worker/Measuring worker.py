from microbit import *

length = 200

class HCSR04:
    def __init__(self, tpin=pin16, epin=pin15):
        spi.init(baudrate=125000, sclk=tpin, mosi=tpin, miso=epin)
        self.r = bytearray(length)

    def distance(self):
        pre = 0
        post = 0
        k = -1
        self.r[0] = 255
        spi.write_readinto(self.r, self.r)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(self.r) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            try:
                k, value = next((ind, v)for ind, v in enumerate(
                                                        self.r[i:length - 2])
                                if self.r[i + ind + 1] == 0)
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist = -1 if i < 0 else round(((pre + (k - i) * 8. + post)*8*0.172)/2)
        return dist

sonar = HCSR04()

while True:
    distance = round(sonar.distance()/10)
    display.scroll(str(distance))
    sleep(500)