# ----------------------------------------
# LAB_0601a (LED Blink with time)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16 Control LED

from machine import Pin
import time

t_ms = [1000, 500, 250, 100, 50]
idx = 0
p16 = Pin(16, Pin.OUT)

while True:
    for i in range(0,5):
        p16.on()
        time.sleep_ms(t_ms[idx])
        p16.off()
        time.sleep_ms(t_ms[idx])
    idx = idx + 1
    if idx > 4:
        idx = 0
