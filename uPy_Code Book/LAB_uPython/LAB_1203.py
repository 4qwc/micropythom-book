# ----------------------------------------
# LAB_1203 (I2C-Memory operations)
# MicroPython book by AppSoftTech
# ----------------------------------------
# 24LC32A (32K I2C™ Serial EEPROM)

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

print('EEPROM Address:', i2c.scan())
time.sleep_ms(100)

eeaddr = 80     # 24LC32A I2C Address
memaddr = 0     # EEPROM Memory Address
buf = 'Hello ESP32 MicroPython Book'

print('Write EEPROM Memory:', buf)
sta = i2c.writeto_mem(eeaddr, memaddr, buf, addrsize=16)
time.sleep_ms(10)

print('Read EEPROM Memory:', end='')
data = i2c.readfrom_mem(eeaddr, memaddr, len(buf), addrsize=16)
print(data)

while True:
    pass
