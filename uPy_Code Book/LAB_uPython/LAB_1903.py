# ----------------------------------------
# LAB_1903 (UART2)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Hardware UART2

from machine import UART, Pin
import time

# UART2 pin: RX2/16, TX2/17 (default)
ser2 = UART(2, baudrate=9600, timeout=50)

led1 = Pin(22, Pin.OUT)
led2 = Pin(23, Pin.OUT)

time.sleep(1)
ser2.write("\nControl LED On/Off!\n")
led1.off()
led2.off()

while True:
    ch = ser2.read()
    if ch == None:
        pass
    else:
        ch = ch.decode("utf-8")
        if ch == 'a': led1.on()
        elif ch == 'b': led1.off()
        elif ch == 'c': led2.on()
        elif ch == 'd': led2.off()
        elif ch == 'e': led1.on(); led2.on()
        elif ch == 'f': led1.off(); led2.off()
        else:
            print('invalid command!')
