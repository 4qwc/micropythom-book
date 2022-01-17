# ----------------------------------------
# LAB_0901a (PWM)
# MicroPython book by AppSoftTech
# ----------------------------------------
# High LED

from machine import Pin, PWM
import time

led = PWM(Pin(15), freq=10000, duty=1023)

while True:
    pass
