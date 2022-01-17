# ----------------------------------------
# LAB_0602 (2 LED Blink)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16 & GPIO17 Control LED

from machine import Pin
import time

led01 = Pin(16, Pin.OUT)
led02 = Pin(17, Pin.OUT)

while True:
    led01.on()
    led02.off()
    time.sleep_ms(500)
    led01.off()
    led02.on()
    time.sleep_ms(500)
