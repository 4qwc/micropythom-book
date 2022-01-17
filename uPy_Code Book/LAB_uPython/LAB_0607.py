# ----------------------------------------
# LAB_0607 (Switch & 2 LED)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO12/Switch & GPIO16/17/LED

from machine import Pin
import time

sw01 = Pin(12, Pin.IN)
led01 = Pin(16, Pin.OUT)
led02 = Pin(17, Pin.OUT)

mem_sw = 0
led01.off()
led02.off()

while True:
    if sw01.value() == 1:
        led01.on()
        if mem_sw == 0:
            led02.on()
        else:
            led02.off()
        mem_sw = ~mem_sw
        while sw01.value():
            time.sleep_ms(10)
    else:
        led01.off()
