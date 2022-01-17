# ----------------------------------------
# LAB_0802a (4-Digit, 7-Segments LED (TM1637))
# MicroPython book by AppSoftTech
# ----------------------------------------

from machine import Pin
import tm1637
import time

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

def show(a, b):

    # show "12:59"
    #tm.numbers(12, 59)
    tm.numbers(a, b)
    time.sleep(1)

    '''
    # all LEDS off
    tm.write([0, 0, 0, 0])
    time.sleep(1)
    '''

    # show temperature '24*C'
    tm.temperature(20)
    time.sleep(1)

    # show "COOL"
    tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])
    time.sleep(1)

m = 19
while True:
    show(1, m)
    m += 3
    time.sleep(1)
