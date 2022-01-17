# ----------------------------------------
# LAB_2002 (LED Toggle)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Control LED Toggle

import led_toggle as led
import time

p23 = led.led_toggle(23)
p22 = led.led_toggle(22)

p22.set(1)
p23.set(0)

while True:
    p23.toggle()
    p22.toggle()
    print('LED Toggle')
    time.sleep_ms(500)

