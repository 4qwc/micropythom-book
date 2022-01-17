# ----------------------------------------
# LAB_1403 (DHT driver)
# MicroPython book by AppSoftTech
# ----------------------------------------
# DHT11 Digital Temperature and Humidity Sensor

from machine import Pin
from time import sleep_ms
import dht

d = dht.DHT11(Pin(14))
sleep_ms(1000)

while True:
    try:
        d.measure()
        temp = d.temperature()    # (°C)
        humi = d.humidity()       # (% RH)
        print('Temp:', temp, ' Humi:', humi)
        sleep_ms(1000)
    except OSError as e:
        print('Failed to read sensor.')
