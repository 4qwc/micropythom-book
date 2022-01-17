# ----------------------------------------
# LAB_1201 (I2C-PCF8574)
# MicroPython book by AppSoftTech
# ----------------------------------------
# PCF8574 (I2C general-purpose I/Os)

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

print('PCF8574 Address:', i2c.scan())
time.sleep_ms(100)

pcfaddr = 32    # PCF8574 I2C Address

while True:
    i2c.writeto(pcfaddr, b'\x00')   # LED ALL ON
    time.sleep_ms(250)
    i2c.writeto(pcfaddr, b'\xFF')   # LED OFF
    time.sleep_ms(100)
    i2c.writeto(pcfaddr, b'\x0E')   # LED LEFT ON
    time.sleep_ms(500)
    i2c.writeto(pcfaddr, b'\xFF')   # LED OFF
    time.sleep_ms(100)
    i2c.writeto(pcfaddr, b'\x07')   # LED RIGHT ON
    time.sleep_ms(500)
    i2c.writeto(pcfaddr, b'\xFF')   # LED OFF
    time.sleep_ms(100)
