# ----------------------------------------
# LAB_1603 (OLED IIC 1306)
# MicroPython book by AppSoftTech
# ----------------------------------------
# OLED 128x64 IIC (SSD1306 driver)

from machine import Pin, I2C
import time
import ssd1306
import framebuf
import dht

width = 128
height = 64

#ref: https://blog.miguelgrinberg.com
def load_image(filename):
    with open(filename, 'rb') as f:
        f.readline()
        f.readline()
        width, height = [int(v) for v in f.readline().split()]
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)

# construct a software I2C bus
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(width, height, i2c)

d = dht.DHT11(Pin(14))

image = load_image('temphumi.pbm')
oled.blit(image, 5, 0)
oled.text('Temp:', 60, 10)
oled.line(60,30, 125,30, 1)
oled.text('Humi:', 60, 40)
oled.show()

while True:
    try:
        d.measure()
        temp = d.temperature()    # (°C)
        humi = d.humidity()       # (% RH)
        print('Temp:', temp, ' Humi:', humi)
        oled.fill_rect(100, 8, 100, 12, 0)
        oled.text(str(temp), 100, 10)
        oled.fill_rect(100, 38, 100, 12, 0)
        oled.text(str(humi), 100, 40)
        oled.show()
        time.sleep_ms(1000)
    except OSError as e:
        print('Failed to read sensor.')
