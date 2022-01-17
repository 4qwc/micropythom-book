# ----------------------------------------
# LAB_1802b (P22 IRQ)
# MicroPython book by AppSoftTech
# ----------------------------------------
# External interrupts (Pin)

import machine
from machine import WDT
import time

p22Cnt = 0
p22Hook = False

p22 = machine.Pin(22, machine.Pin.IN)
p23 = machine.Pin(23, machine.Pin.OUT)

wdt = WDT(id=0, timeout=5000)  # enable it with a timeout of 5s
wdt.feed()

def p22_handler(pin):
    global p22Cnt, p22Hook
    p22Cnt = p22Cnt +1
    p22Hook = True
    print(p22Cnt, end=' ')

def pin_irq(state):
    if state == True:
        p22.irq(handler=p22_handler, trigger=machine.Pin.IRQ_RISING)
    else:
        p22.irq(trigger=0)

# --------------------------------------------
pin_irq(True)

while True:
    p23.on()
    time.sleep_ms(1000)
    p23.off()
    time.sleep_ms(1000)
    wdt.feed()
    if p22Hook == True:
        print('\nInterrupt Counter', p22Cnt)
        p22Hook = False
        print('wait...5 seconds')
        wdt.feed()
        state=machine.disable_irq()
        time.sleep_ms(300)
        machine.enable_irq(state)
