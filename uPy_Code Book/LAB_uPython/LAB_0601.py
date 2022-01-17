# ----------------------------------------
# LAB_0601 (LED Blink)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16 Control LED

from machine import Pin
import time

p16 = Pin(16, Pin.OUT)

while True:
    p16.on()
    time.sleep_ms(500)
    p16.off()
    time.sleep_ms(500)
