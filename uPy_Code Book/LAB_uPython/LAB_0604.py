# ----------------------------------------
# LAB_0604 (4 LED control)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16,17,18 & 19 Control LED

from machine import Pin
import time

led = []
t_ms = 100

for i in range(0, 4):
    led.append(Pin(16+i, Pin.OUT))

while True:
    for i in range(0, 4):
        led[i].on()
        time.sleep_ms(t_ms)
        led[i].off()
        time.sleep_ms(t_ms)

    for i in range(2, 0, -1):
        led[i].on()
        time.sleep_ms(t_ms)
        led[i].off()
        time.sleep_ms(t_ms)
