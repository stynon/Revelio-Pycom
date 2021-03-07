from network import WLAN
import machine
import pycom
import request


wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)

def connectWifi():
    wlan.connect(ssid='telenet-4D87F74', auth=(WLAN.WPA2, 'x2UcakjTsryz'))
    while not wlan.isconnected():
        pycom.rgbled(0xFF0000)
    print("WiFi connected succesfully")
    pycom.rgbled(0x007F00)
    print(wlan.ifconfig())
