# ----------------------------------------
# LAB_1802a (P22 IRQ)
# MicroPython book by AppSoftTech
# ----------------------------------------
# External interrupts (Pin)

import machine
import time

state = 0.0
p22Cnt = 0
p22Hook = False

p22 = machine.Pin(22, machine.Pin.IN)
p23 = machine.Pin(23, machine.Pin.OUT)

def p22_hanlder(pin):
    global p22Cnt, p22Hook
    p22Cnt = p22Cnt +1
    p22Hook = True
    print(p22Cnt, end=' ')

p22.irq(handler=p22_handler, trigger=machine.Pin.IRQ_RISING)

# --------------------------------------------
while True:
    p23.on()
    time.sleep_ms(1000)
    p23.off()
    time.sleep_ms(1000)

    if p22Hook == True:
        state = machine.disable_irq()
        print('\nInterrupt Counter', p22Cnt)
        p22Hook = False
        #time.sleep(5)      # uncommend this line *** Guru Meditation Error *****
        machine.enable_irq(state)
        print('wait...5 seconds')
        time.sleep(5)

