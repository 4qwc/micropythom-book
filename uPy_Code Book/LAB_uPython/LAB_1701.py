# ----------------------------------------
# LAB_1701 (Blynk IoT)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Blynk library VERSION = "0.2.6"

from machine import Pin
import time
import network
import blynklib_mp as BlynkLib

WIFI_SSID  = 'YourWifiSSID'
WIFI_PASS  = 'YourWifiPassword'
BLYNK_AUTH = 'YourAuthToken'

class sw_press:
    num = 0
    time = 0

def callback(pin):
    print('Switch event on {}'.format(pin), end=' ')
    sw_press.num += 1
    sw_press.time = time.time()
    print("#{} press at {} ".format(sw_press.num, sw_press.time))

led1 = Pin(18, Pin.OUT)  # GPIO18
led2 = Pin(19, Pin.OUT)  # GPIO19
sw1  = Pin(23, Pin.IN)   # GPIO23
sw1.irq(trigger=Pin.IRQ_RISING, handler=callback)

# --------------------------------------------
# Connect network
print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

# --------------------------------------------
# Initialize Blynk
print("Connecting to Blynk server...")
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# --------------------------------------------
# Register Virtual Pins
@blynk.handle_event('write V2')
def led2_write_handler(vpin, values):
    if values:
        print('Current vpin {} value: {}'.format(vpin, values[0]))
        if int(values[0]) == 1:
            led2.on()
        else:
            led2.off()

@blynk.handle_event('read V3')
def sw1_read_handler(vpin):
    print('Read event on vpin {} '.format(vpin))
    blynk.virtual_write(vpin, "#{} press at {} ".format(sw_press.num, sw_press.time))

sw1_status = 1

while True:
    blynk.run()
    if sw1.value() == 0: # Read switch button
        blynk.virtual_write(1, 255)     # LED (V1) HIGH
        led1.on()
        sw1_status = 1
    else:
        if sw1_status != 0:
            blynk.virtual_write(1, 50)  # LED (V1) LOW
            led1.off()
            sw1_status = 0
