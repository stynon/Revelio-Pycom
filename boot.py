from network import WLAN
import machine
import pycom
import time
wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)

wlan.connect(ssid='SSID', auth=(WLAN.WPA2, 'Password'))
while not wlan.isconnected():
    pycom.rgbled(0xFF0000)
print("WiFi connected succesfully")
pycom.rgbled(0x007F00)
time.sleep(2)
print(wlan.ifconfig())
