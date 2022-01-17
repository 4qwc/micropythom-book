# ----------------------------------------
# LAB_1001 (PWM)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Servo Motor Control

from machine import Pin, PWM, ADC
import time

# create PWM object on I/O pin
servo = PWM(Pin(12), freq=50)

# create ADC object on ADC pin
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    adc = pot.read()
    print('pot:', adc, end=' >> ')
    duty = map(adc, 0, 4095, 27, 120)
    servo.duty(duty)    # position
    pos = map(duty, 27, 120, 0, 180)
    print('Servo Position:', pos)
    time.sleep_ms(100)
