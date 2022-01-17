# ----------------------------------------
# LAB_0606 (2 Switch & LED)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO12/13/Switch & GPIO16/LED

from machine import Pin
import time

led01 = Pin(16, Pin.OUT)
sw01 = Pin(12, Pin.IN)
sw02 = Pin(13, Pin.IN)

led01.value(0)

while True:
    if sw01.value() == 1:
        led01.value(1)
    elif sw02.value() == 1:
        led01.value(0)
