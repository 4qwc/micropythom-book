# ----------------------------------------
# LAB_1203a (I2C-Memory operations)
# MicroPython book by AppSoftTech
# ----------------------------------------
# 24LC32A (32K I2C™ Serial EEPROM)

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

ee_addr = 80    # I2C 24LC32A Address
memaddr = 0     # EEPROM Memory Address
buf = 28        # bytes read

print('Read EEPROM Memory:', end='')
data = i2c.readfrom_mem(ee_addr, memaddr, buf, addrsize=16)
print(data)

while True:
    pass
