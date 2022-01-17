# ----------------------------------------
# LAB_0605 (Switch & LED)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO12/Switch & GPIO16/LED

from machine import Pin
import time

led01 = Pin(16, Pin.OUT)
sw01 = Pin(12, Pin.IN)

while True:
    sw = sw01.value()
    if sw == 1:
        led01.on()
    else:
        led01.off()
