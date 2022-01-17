# ----------------------------------------
# LAB_0702 (Keypad)
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

n_row = [14, 13, 11, 7]

for col in range(0, 4):
    p_col[col].on()

while True:
    for col in range(0,4):
        p_col[col].off()
        key = (
            (p_row[3].value() << 3)
            | (p_row[2].value() << 2)
            | (p_row[1].value() << 1)
            | (p_row[0].value())
        )
        p_col[col].on()
        if key != 15:
            if key in n_row:
                row = n_row.index(key)
                print("(R:", row , "C:", col, end="),")
                time.sleep_ms(500)

    time.sleep_ms(5)
