# ----------------------------------------
# LAB_1501 (ThingSpeak IoT)
# MicroPython book by AppSoftTech
# ----------------------------------------
# ThingSpeak for IoT (https://thingspeak.com/)
# DHT11 Digital Temperature and Humidity Sensor

from machine import Pin
import network, time
import dht

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
            print("not....")
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

API_KEY = 'V8AXNV53GR7X7YA1'
channel_1 = 'DHT11'               # DHT11 Channel
field_temp = 'Temp'
field_Humi = 'Humi'

thing_speak = ThingSpeakAPI([
    Channel(channel_1, API_KEY, [field_temp, field_Humi])],
    protocol_class=ProtoHTTP, log=True)

d = dht.DHT11(Pin(14))

# --------------------------------------------
# main
temp = 0
humi = 0
while True:

    status = True
    try:
        d.measure()
        temp = d.temperature()      # (°C)
        humi = d.humidity()         # (% RH)
        print('Temp:', temp, ' Humi:', humi)
        status = True
        #time.sleep_ms(1000)
    except OSError as e:
        status = False
        print('Failed to read sensor.')

    try:
        thing_speak.send(channel_1, {field_temp: temp, field_Humi: humi})
        time.sleep(thing_speak.free_api_delay)
    except:
        print('WLan Connect Aborted..')
