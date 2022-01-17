# ----------------------------------------
# LAB_2001 (LED Blink)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16 Control LED

from machine import Pin
import time

p16 = Pin(16, Pin.OUT)

while True:
    p16.on()
    print('GPIO16 LED ON')
    time.sleep_ms(500)
    p16.off()
    print('GPIO16 LED OFF')
    time.sleep_ms(500)
    
