import ultrasonic
import wifiConnect
import loraWan
import time
import wifiAdafruit
import request

#use this for datasending over loraWan
loraWan.loraConnect()
ultrasonic.defuart()
while True:
    ultrasonic.defuart()
    distance = ultrasonic.readSensor()
    loraWan.send(distance)
    print(distance)
    time.sleep(10)

#use this for datasending over wifi
#wifiConnect.connectWifi()
#ultrasonic.defuart()
#while True:
#    print(1)
#    ultrasonic.defuart()
#    print(2)
#    distance = ultrasonic.readSensor()
#    print(3)
#    wifiAdafruit.sendDataWifi(distance)
#    print(4)
#    time.sleep(10)
