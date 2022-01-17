# ----------------------------------------
# LAB_1203c (I2C-Memory operations)
# MicroPython book by AppSoftTech
# ----------------------------------------
# 24LC32A (32K I2C™ Serial EEPROM)

from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

print('EEPROM Address:', i2c.scan())
time.sleep_ms(100)

ee_addr = 80    # I2C 24LC32A Address
memaddr = 0     # EEPROM Memory Address
buf = ''        # buf write/read

for i in range(0, 16):
    buf = buf + chr(i)

print('Write EEPROM Memory:', bytes(buf, 'utf8'))
i2c.writeto_mem(eeaddr, memaddr, buf, addrsize=16)
time.sleep_ms(10)

print('Read EEPROM Memory:', end='')
data = i2c.readfrom_mem(eeaddr, memaddr, len(buf), addrsize=16)
print(data)

while True:
    pass
