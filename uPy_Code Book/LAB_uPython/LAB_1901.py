# ----------------------------------------
# LAB_1901 (UART1)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Hardware UART1

from machine import UART
import time

ser1 = UART(1, baudrate=9600, rx=22, tx=23, timeout=100)

time.sleep(1)
ser1.write("\nHello, UART#1!\n")

while True:
    ch = ser1.read()
    if ch == None:
        pass
    else:
        print('Read:', ch)
        str = ch.decode("utf-8")
        if str == 'z':
            break

print('\nExit read ser1')
while True:
    pass
