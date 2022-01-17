# ----------------------------------------
# LAB_1801 (P22 IRQ)
# MicroPython book by AppSoftTech
# ----------------------------------------
# External interrupts (Pin)

from machine import Pin
import time

p22Cnt = 0
p22Hook = False

p22 = Pin(22, Pin.IN)
p23 = Pin(23, Pin.OUT)

def p22_handler(pin):
    global p22Cnt, p22Hook
    p22Cnt = p22Cnt +1
    p22Hook = True
    print(p22Cnt, end=' ')

p22.irq(handler=p22_handler, trigger=Pin.IRQ_RISING)

while True:
    p23.on()
    time.sleep_ms(250)
    p23.off()
    time.sleep_ms(250)
    if p22Hook == True:
        print('\nInterrupt Counter', p22Cnt)
        p22Hook = False
        print('wait...5 seconds')
        time.sleep(5)


