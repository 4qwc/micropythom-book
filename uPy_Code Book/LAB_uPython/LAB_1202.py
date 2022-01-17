# ----------------------------------------
# LAB_1202 (I2C-PCF8574)
# MicroPython book by AppSoftTech
# ----------------------------------------
# PCF8574 (I2C general-purpose I/Os)

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

print('PCF8574 Address:', i2c.scan())
time.sleep_ms(100)

pcfaddr = 32     # PCF8574 I2C Address

#---------------------------------------------
# Convert bytes to int or int to bytes in python
# Ref: https://coderwall.com/p/x6xtxq/convert-bytes-to-int-or-int-to-bytes-in-python
def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
#---------------------------------------------

while True:
    data = i2c.readfrom(pcfaddr, 1)
    bits = (bin(bytes_to_int(data)))

    if int(bits) & 0b10000:
        i2c.writeto(pcfaddr, b'\x0A')     # write 0x0A to PCF8574
        print('SW1 press:', bits)
    elif int(bits) & 0b100000:
        i2c.writeto(pcfaddr, b'\x05')     # write 0x05 to PCF8574
        print('SW2 press:', bits)
    else:
        i2c.writeto(pcfaddr, b'\x0F')     # write 0x0F to PCF8574
        print('No press', bits)

    time.sleep_ms(100)

