# ----------------------------------------
# LAB_1902 (UART2)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Hardware UART2

from machine import UART, Pin
import time

# UART2 pin: RX2/16, TX2/17 (default)
ser2 = UART(2, baudrate=9600, timeout=2000)

led1 = Pin(22, Pin.OUT)
led2 = Pin(23, Pin.OUT)

time.sleep(1)
ser2.write("\nHello, UART#2!\n")

def led_toggle(pin):
    pin.value(not pin.value())

led1.on()
led2.off()

while True:
    ch = ser2.readline()
    if ch == None:
        led_toggle(led1)
    else:
        led_toggle(led2)
        print('ESP32 read:', ch)
        ser2.write('\nESP send: ')
        ser2.write(ch)
