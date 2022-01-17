# ----------------------------------------
# LAB_1103 (ADC)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Potentiometer & I2C 16x2 LCD

from machine import Pin, ADC, I2C
from time import sleep_ms
from lcd_i2c_esp32 import I2cLcd

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.putstr("ADC:\n")
lcd.putstr("Vol:")

# create ADC object on ADC pin
pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)

while True:
    val = pot.read()
    lcd.move_to(5, 0)           # Row, Column
    lcd.putstr("%-5d" %(val))
    lcd.move_to(5, 1)           # Row, Column
    voltage = str((val*3.3)/4059)
    lcd.putstr("%sV" %(voltage[0:3]))
    sleep_ms(500)
