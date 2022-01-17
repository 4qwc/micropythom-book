# ----------------------------------------
# LAB_1002 (Stepper Motor)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Stepper Motor 28BYJ-48 Control

from machine import Pin
import Stepper
import time

# PIN map: INx/GPIOm:
IN1 = Pin(26, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(17, Pin.OUT)
IN4 = Pin(16, Pin.OUT)

stepM1 = Stepper.create(IN1, IN2, IN3, IN4, delay=2)

print('Stepper Motor')
while True:
    print('>>Step: 100 forward')
    stepM1.step(100)
    time.sleep_ms(100)
    print('>>Step: 100 backward')
    stepM1.step(100,-1)
    time.sleep_ms(100)
    print('>>Angle: 180 forward')
    stepM1.angle(180)
    time.sleep_ms(100)
    print('>>Angle: 360 backward')
    stepM1.angle(360,-1)
    time.sleep_ms(100)
