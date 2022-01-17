# ----------------------------------------
# LAB_0601b (Fading an LED)
# MicroPython book by AppSoftTech
# Ref: https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html
# ----------------------------------------
# Fading an LED

from machine import Pin, PWM
import time
import math

led = PWM(Pin(16), freq=1000, duty=0)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

while True:
    pulse(led, 50)
    time.sleep(1)
    for i in range(10):
        pulse(led, 20)

