# -----
# lib_gpio (GPIO Library)
# MicroPython book by AppSoftTech
# -----

from micropython import const
from machine import Pin

class LED13(object):
    def __init__(self):
        self.p = Pin(13, Pin.OUT)

    def led13(self,i):
        if i == 1:
            self.p.on()
        else:
            self.p.off()
