# ----------------------------------------
# LAB_1101 (ADC)
# MicroPython book by AppSoftTech
# ----------------------------------------
# 2-Axis Joystick Control

from machine import Pin, PWM, ADC
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
    VRx = joyX.read()
    VRy = joyY.read()
    print('VRx:', VRx, 'VRy:', VRy, 'SW:', sw)
    time.sleep_ms(50)
