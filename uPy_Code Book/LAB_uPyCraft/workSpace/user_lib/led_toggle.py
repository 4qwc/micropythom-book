# LED Toggle Class
# Prajin Palangsantikul

from machine import Pin

class led_toggle:

    def __init__(self, pin):
        self.pin = pin
        self.pin = Pin(pin, Pin.OUT)

    def set(self, val):
        self.pin.value(val)

    def toggle(self):
        self.pin.value(not self.pin.value())

