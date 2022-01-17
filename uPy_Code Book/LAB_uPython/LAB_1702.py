# ----------------------------------------
# LAB_1702 (Blynk IoT)
# MicroPython book by AppSoftTech
# ----------------------------------------
# Blynk library VERSION = "0.2.6"

from machine import Pin
import time
import network
import blynklib_mp as BlynkLib
import dht

WIFI_SSID  = 'YourWifiSSID'
WIFI_PASS  = 'YourWifiPassword'
BLYNK_AUTH = 'YourAuthToken'

T_COLOR   = '#ED9D00'
H_COLOR   = '#04C0F8'
ERR_COLOR = '#404040'
T_VPIN    = 1
H_VPIN    = 2
GT_VPIN   = 3
GH_VPIN   = 4
DHT11_PIN = 14

class dhtxx:
    Temp = 0.0
    Humi = 0.0

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
# Initialize Blynk (Free)
print("Connecting to Blynk server free...")
blynk = BlynkLib.Blynk(BLYNK_AUTH, server='blynk.iot-cm.com', port=8080)

# --------------------------------------------
# Initialize DHT11 Sensor
dht11 = dht.DHT11(Pin(DHT11_PIN, Pin.IN, Pin.PULL_UP))

# --------------------------------------------
# Register Virtual Pins
@blynk.handle_event('read V{}'.format(T_VPIN))
def read_handler(vpin):
    dhtxx.Temp = 0.0
    dhtxx.Humi = 0.0
    # read sensor data
    try:
        dht11.measure()
        dhtxx.Temp = dht11.temperature()
        dhtxx.Humi = dht11.humidity()
    except OSError as o_err:
        print("Unable to get DHT11 sensor data: '{}'".format(o_err))

    # change widget values and colors according read results
    if dhtxx.Temp != 0.0 and dhtxx.Humi != 0.0:
        blynk.set_property(T_VPIN, 'color', T_COLOR)
        blynk.set_property(H_VPIN, 'color', H_COLOR)
        blynk.set_property(GT_VPIN, 'color', T_COLOR)
        blynk.set_property(GH_VPIN, 'color', H_COLOR)
        blynk.virtual_write(T_VPIN, dhtxx.Temp)
        blynk.virtual_write(H_VPIN, dhtxx.Humi)
        blynk.virtual_write(GH_VPIN, dhtxx.Humi)
        blynk.virtual_write(GT_VPIN, dhtxx.Temp)
    else:
        # show widgets aka 'disabled' that mean we had errors
        # during read sensor operation
        blynk.set_property(T_VPIN, 'color', ERR_COLOR)
        blynk.set_property(H_VPIN, 'color', ERR_COLOR)

while True:
    blynk.run()
    print("DHT11 sensor data: Temp:{}, Humi:{}".format(dhtxx.Temp, dhtxx.Humi))

