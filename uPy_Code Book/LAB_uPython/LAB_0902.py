# ----------------------------------------
# LAB_0902 (PWM)
# MicroPython book by AppSoftTech
# ----------------------------------------
# DC Motor Control + L9110 Fan Motor Keyes Board

from machine import Pin, PWM, ADC
import time

# create PWM object on I/O pin
INA = PWM(Pin(18), freq=1000, duty=0)
INB = PWM(Pin(19), freq=1000, duty=0)

# ---
pot = ADC(Pin(35))
# ---
pot.atten(ADC.ATTN_11DB)
# ---
pot.width(ADC.WIDTH_12BIT)

# ---
def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

medium = 2030   # ADC: 0(Min), 4095(Max)
gap = 200       # +/- Gap
duty = 0        # Duty cycle

while True:
    adc = pot.read()
    print('ADC:', adc, end=' >> ')
    if adc > (medium + gap):
        duty = map(adc, (medium + gap), 4095, 0, 1023)
        print('INA duty:', duty)
        INA.duty(duty)      # set speed motor
        INB.duty(0)         # stop motor

    elif adc < (medium - gap):
        duty = map(adc, (medium - gap), 0, 0, 1023)
        print('INB duty:', duty)
        INA.duty(0)         # stop motor
        INB.duty(duty)      # set speed motor

    else:
        print('Motor Stop..')
        INA.duty(0)         # stop motor
        INB.duty(0)         # stop motor

    time.sleep_ms(100)
