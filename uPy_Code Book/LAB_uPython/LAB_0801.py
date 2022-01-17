# ----------------------------------------
# LAB_0801 (7-Segments LED)
# MicroPython book by AppSoftTech
# ----------------------------------------

from machine import Pin
import time

# 0,1,2,3,4,5,6,7,8,9,A,b,C,d,E,F,.
led_num = (0x3F, 0x06, 0x5B, 0x4F, 0x66,
           0x6D, 0x7D, 0x07, 0x7F, 0x6F,
           0x77, 0x7C, 0x39, 0x5E, 0x79,
           0x71, 0x80)

gpio = (15, 2, 4, 16, 17, 5, 18, 19)    # gpio pins
led = []                                # list empty

for i in range(0, len(gpio)):
    led.append(Pin(gpio[i], Pin.OUT))   # adds an item to list.

def play7SegLED(num):
    segment = led_num[num]
    for i in range(8):
        if segment & 0b1:
            led[i].on()
        else:
            led[i].off()
        segment >>= 1

i = 0
while True:
    play7SegLED(i)
    time.sleep_ms(250)
    i += 1
    if i > 15:
        i = 0
