# ----------------------------------------
# LAB_1401 (OneWire driver)
# MicroPython book by AppSoftTech
# ----------------------------------------
# DS18B20 1-Wire Digital Thermometer

from machine import Pin
import time
import onewire, ds18x20

ow = onewire.OneWire(Pin(12))   # the device is on GPIO12
ds = ds18x20.DS18X20(ow)

# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

while True:
    print('temperatures:', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(bytes(rom), ':', ds.read_temp(rom))

    time.sleep_ms(100)

