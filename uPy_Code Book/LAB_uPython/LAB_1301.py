# ----------------------------------------
# LAB_1301 (SPI)
# MicroPython book by AppSoftTech
# ----------------------------------------
# LED Dot Matrix 8x8 MAX7219 IC Driver Module

from machine import Pin, SPI
import time
import max7219

# MAX7219 - GPIO pin
CS = Pin(12)
DIN = Pin(13)
CLK = Pin(14)

hspi = SPI(1, 10000000, sck=CLK, mosi=DIN)
display = max7219.Matrix8x8(hspi, CS, 1)
display.brightness(1)   # Brightness range (0-15)

while True:
    for i in range(0, 10):
        display.fill(0)
        display.text(str(i),0,0,1)
        display.show()
        time.sleep_ms(250)

    for i in range(ord('A'), ord('Z')+1):
        display.fill(0)
        display.text(chr(i),0,0,1)
        display.show()
        time.sleep_ms(250)
