import request
import time

username = 'stynon'
feed_name = 'ttn'
aio_key = 'aio_ATJi25ki7z8WfIOUlXww9IoKJsS2'
url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'

def sendDataWifi(data):
    body = {'value': str(data)}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = request.post(url, json=body, headers=headers)
        print(r.text)
        time.sleep(10)
    except Exception as e:
        print(e)
