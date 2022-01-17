# ----------------------------------------
# LAB_1302 (SPI)
# MicroPython book by AppSoftTech
# ----------------------------------------
# 74HC595 8-bit shift register with output latches; 3-state

from machine import Pin, SPI
import time

# 74HC595 - GPIO pin
STCP = Pin(12, Pin.OUT) # Latch
DS   = Pin(13)          # MOSI
SHCP = Pin(14)          # SCK

hspi = SPI(1, 10000000, sck=SHCP, mosi=DS)

def spi_write(data):
    hspi.write(data)
    STCP.on()           # Latch (Display result)
    time.sleep_us(1)
    STCP.off()

spi_write(b'\xFF')
time.sleep(1)

while True:
    spi_write(b'\xAA')     # write 0xAA bytes on MOSI
    time.sleep_ms(500)
    spi_write(b'\x55')     # write 0x55 bytes on MOSI
    time.sleep_ms(500)

