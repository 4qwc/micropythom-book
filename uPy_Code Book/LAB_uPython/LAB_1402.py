# ----------------------------------------
# LAB_1402 (NeoPixel driver)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Neopixel LED

from machine import Pin
import time
from neopixel import NeoPixel

pin = Pin(12, Pin.OUT)   # set GPIO12 to output to drive NeoPixels
np = NeoPixel(pin, 12)   # create NeoPixel driver on GPIO12 for 12 pixels

Black   = (0,0,0)
White   = (255,255,255)
Red     = (255,0,0)
Lime    = (0,255,0)
Blue    = (0,0,255)
Yellow  = (255,255,0)
Cyan    = (0,255,255)
Magenta = (255,0,255)
Silver 	= (192,192,192)
Gray 	= (128,128,128)
Maroon 	= (128,0,0)
Olive 	= (128,128,0)
Green 	= (0,128,0)
Purple 	= (128,0,128)
Teal 	= (0,128,128)
Navy 	= (0,0,128)

color = (Navy, Teal, Purple, Green, Olive, Maroon, Gray, Silver,
         Magenta, Cyan, Yellow, Blue, Lime, Red, White, Black)

while True:
    for i in range(0, 12):
        np[i] = color[i]        # set the i pixel to color[c]
        np.write()              # write data to all pixels
        time.sleep_ms(200)

    for i in range(0, 12):
        np[i] = Black
        np.write()
        time.sleep_ms(100)

