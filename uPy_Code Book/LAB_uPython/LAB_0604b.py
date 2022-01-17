# ----------------------------------------
# LAB_0604 (4 LED control)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16-GPIO18 Control LED

from machine import Pin
import time

pin_gpio = []
t_ms = 100

for i in range(0, 4):
    pin_gpio.append(Pin(16+i, Pin.OUT))

while True:
    for led in pin_gpio:
        print(led)
        led.on()
        time.sleep_ms(t_ms)
        led.off()
        time.sleep_ms(t_ms)
