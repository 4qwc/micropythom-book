# ----------------------------------------
# LAB_1102 (ADC)
# MicroPython book by AppSoftTech
# ----------------------------------------
# 2-Axis Joystick Control

from machine import Pin, ADC
import time

# create ADC object on ADC pin
joyX = ADC(Pin(35))
joyY = ADC(Pin(34))
joyX.atten(ADC.ATTN_11DB)
joyY.atten(ADC.ATTN_11DB)

# create Pin object on GPIO pin
sw13 = Pin(13, Pin.IN,Pin.PULL_UP)

while True:
    sw = sw13.value()
    if sw == 1:
        sw = 1000
    VRx = joyX.read()
    VRy = joyY.read()
    print((VRx, VRy, sw))
    time.sleep_ms(50)
