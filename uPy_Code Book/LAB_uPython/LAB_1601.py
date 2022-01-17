# ----------------------------------------
# LAB_1601 (OLED IIC 1306)
# MicroPython book by AppSoftTech
# ----------------------------------------
# OLED 128x64 IIC (SSD1306 driver)

from machine import Pin, I2C
import time
import ssd1306

width = 128
height = 64

# construct a software I2C bus
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(width, height, i2c)

oled.text('Hello... AST!', 0, 0)
oled.text('MicroPython Book', 0, 15)
oled.text('appsofttech.com', 0, 30)
oled.show()
time.sleep(2)

w = int(width/2)
h = int(height/2)

while True:
    for i in range(8):
        print(i)
        oled.fill(0)
        if i == 0:
            oled.fill(1)
            oled.text('fill', 0, 5, 0)
        elif i == 1:
            oled.text('rect', 0, 0)
            oled.rect(0, 20, w, h, 1)
        elif i == 2:
            oled.text('fill_rect', 0, 0)
            oled.fill_rect(0, 20, w, h, 1)
        elif i == 3:
            oled.text('line', 0, 0)
            oled.line(0, 20, width, height, 1)
        elif i == 4:
            oled.text('vline', 0, 0)
            oled.vline(0, 20, height, 1)
        elif i == 5:
            oled.text('hline', 0, 0)
            oled.hline(0, 20, width, 1)
        elif i == 6:
            oled.text('pixel', 0, 0)
            oled.pixel(w, h, 1)
        elif i == 7:
            oled.text('scroll', 0, 0)
            oled.scroll(10, 10)
        oled.show()
        time.sleep(1)
