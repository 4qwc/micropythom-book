# ----------------------------------------
# LAB_0603 (LED Blink on time)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Use GPIO16,17 & 18 Control LED

from machine import Pin
import time

led01 = Pin(16, Pin.OUT); led02 = Pin(17, Pin.OUT);
led03 = Pin(18, Pin.OUT)
t_ms = [1000, 500, 250, 100, 50]
cnt = i = 0

while True:
    led01.on(); led02.on(); led03.on()
    time.sleep_ms(t_ms[i])
    led01.off(); led02.off(); led03.off()
    time.sleep_ms(t_ms[i])
    print(cnt, end= ", ")
    cnt = cnt + 1
    if cnt == 5:
        cnt = 0
        print(" >", i)
        print("----------------")
        i += 1
        if i > 4:
            i = 0
