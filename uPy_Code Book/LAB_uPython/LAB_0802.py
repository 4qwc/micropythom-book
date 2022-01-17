# ----------------------------------------
# LAB_0802 (4-Digit, 7-Segments LED (TM1637))
# MicroPython book by AppSoftTech
# ----------------------------------------

from machine import Pin
import tm1637
import time, esp32

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

def tempShow(temp):
    # show temperature
    tm.temperature(temp)

while True:
    tf = esp32.raw_temperature()    # Fahrenheit
    tc = (tf-32.0)/1.8              # Fahrenheit to Celsius
    tempShow(int(tc))
    print('F:',tf, ',C:', tc)
    time.sleep(1)

