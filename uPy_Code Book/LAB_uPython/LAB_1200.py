# ----------------------------------------
# LAB_1200 (I2C-PCF8574)
# MicroPython book by AppSoftTech
# ----------------------------------------
# PCF8574 (I2C general-purpose I/Os)

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

print('PCF8574 Address:', i2c.scan())
time.sleep_ms(100)

while True:
    pass
