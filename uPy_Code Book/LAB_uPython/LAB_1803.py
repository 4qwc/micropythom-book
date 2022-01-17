# ----------------------------------------
# LAB_1803 (Hardware Timer)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Hardware Timer0

from machine import Pin
from machine import Timer
import time

pin23 = Pin(23, Pin.OUT)

def tim0_callback(timer):
    pin23.on()
    print('..Timer0 callback - LED ON')

tim0 = Timer(0)
tim0.init(period=500, mode=Timer.PERIODIC, callback=tim0_callback)

while True:
    pin23.off()
    print('..time.sleep_ms - LED OFF')
    time.sleep_ms(1000)
