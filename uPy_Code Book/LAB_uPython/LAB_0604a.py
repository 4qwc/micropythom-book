# ----------------------------------------
# LAB_0604a (4 LED control)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO1-GPIO18 Control LED

from machine import Pin
import time

led = [Pin(16, Pin.OUT), Pin(17, Pin.OUT),
       Pin(18, Pin.OUT), Pin(19, Pin.OUT)]
t_ms = 20

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
