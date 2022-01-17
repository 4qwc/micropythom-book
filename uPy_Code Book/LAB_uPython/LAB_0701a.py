# ----------------------------------------
# LAB_0701a (Keypad)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO18/5/17/16(R1/2/3/4)
# ... GPIO19/21/22/23(C1/2/3/4)

from machine import Pin
import time

pIn = Pin.IN
pUp = Pin.PULL_UP
pOut = Pin.OUT

p_row = [Pin(18, pIn, pUp), Pin(5, pIn, pUp),
        Pin(17, pIn, pUp), Pin(16, pIn, pUp)]
p_col = [Pin(19, pOut), Pin(21, pOut),
        Pin(22, pOut), Pin(23, pOut)]

for col in range(0, 4):
    p_col[col].on()

while True:
    for col in range(0, 4):
        p_col[col].off()
        key = (
            (p_row[3].value() << 3)
            | (p_row[2].value() << 2)
            | (p_row[1].value() << 1)
            | (p_row[0].value())
        )
        p_col[col].on()
        if key != 15:
            #print("(", key, ":", col, end="), ")
            print("(", key, ":", bin(key), ":", col, "), ")
            #print("(", key, ":", bin(key), ":", col, end="), ")
            time.sleep_ms(500)
        #else:
        #    print(key, bin(key))

    time.sleep_ms(10)
