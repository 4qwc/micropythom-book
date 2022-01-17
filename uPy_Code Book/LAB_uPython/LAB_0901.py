# ----------------------------------------
# LAB_0901 (PWM)
# MicroPython book by AppSoftTech
# ----------------------------------------
# LED Dimmer with PWM

from machine import Pin, PWM
import time

led = PWM(Pin(15), freq=10000, duty=0)

duty = 0
while True:
    led.duty(duty)    # set duty cycle
    time.sleep_ms(100)
    duty += 50          # change duty cycle
    if duty >1023:
        duty = 0
