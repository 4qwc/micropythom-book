# ----------------------------------------
# LAB_1502 (ThingSpeak IoT)
# MicroPython book by AppSoftTech
# ----------------------------------------
# ThingSpeak for IoT (https://thingspeak.com/)
# Random Number

import network, time
from urandom import *

# --------------------------------------------
# https://rntlab.com/question/generating-random-in-micropython-for-esp/
def rand( floor, mod=0, negative = False):
    # return random value from -floor.mod to floor.nod if negative is True
    from os import urandom as rnd
    sign = 1 if ord(rnd(1))%10 > 5 else -1
    sign = sign if negative else 1
    if mod:
        value = float(('{}.{}').format(ord(rnd(1))%floor, ord(rnd(1))%mod))
    else:
        value = int(('{}').format(ord(rnd(1))%floor))
    return sign*value

# --------------------------------------------
print('Section: Connect network..')

essid = 'ssid_name'          # Your SSID
password = 'password'        # Your Password
wifi_connect = 1

sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)

wifi_name = sta_if.scan()   # Scan for available access points
for i in range(0,len(wifi_name)):
    #print(wifi_name[i][0])
    if 'Jin' == (wifi_name[i][0]).decode():
        print("Found Wifi:", (wifi_name[i][0]).decode())

time.sleep(5)
while True:
    if wifi_connect == 1:
        # Check for successful connection
        print('connecting to network...')
        sta_if.connect(essid, password)   # Connect to an AP
        time.sleep(1)                     # delay.. response
        if not sta_if.isconnected():
            print("....")
        else:
            print('network config:', sta_if.ifconfig())
            wifi_connect = 0
    else:
        break
    time.sleep(1)

# --------------------------------------------
print('Section: ThingSpeak..')
try:
    from thingspeak import ThingSpeakAPI, Channel, ProtoHTTP
except ImportError:
    from .lib.thingspeak import ThingSpeakAPI, Channel, ProtoHTTP

API_KEY = '8SPY8C2PSVQYVA57'
channel_1 = 'DHT11'               # DHT11 Channel
field_temp = 'Temp'
field_Humi = 'Humi'

thing_speak = ThingSpeakAPI([
    Channel(channel_1, API_KEY, [field_temp, field_Humi])],
    protocol_class=ProtoHTTP, log=True)

# --------------------------------------------
# main
while True:
    num1 = rand(50)
    num2 = rand(50)
    print('Random number:', num1, num2)
    try:
        thing_speak.send(channel_1, {field_temp: num1, field_Humi: num2})
        time.sleep(thing_speak.free_api_delay)
    except:
        print('WLan Connect Aborted..')
        time.sleep_ms(100)
