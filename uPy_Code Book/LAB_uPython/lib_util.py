# -----
# lib_util (Utility Library)
# MicroPython book by AppSoftTech
# -----

from micropython import const
from urandom import *

class UTIL:

    def __init__(self):
        pass

    # --------------------------------------------
    # https://rntlab.com/question/generating-random-in-micropython-for-esp/
    def rand(self, floor, mod=0, negative = False):
        # return random value from -floor.mod to floor.nod if negative is True
        from os import urandom as rnd
        sign = 1 if ord(rnd(1))%10 > 5 else -1
        sign = sign if negative else 1
        if mod:
            value = float(('{}.{}').format(ord(rnd(1))%floor, ord(rnd(1))%mod))
        else:
            value = int(('{}').format(ord(rnd(1))%floor))
        return sign*value

    def read_rand(self, floor):
        return rand(floor)
