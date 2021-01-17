# Gerçek Zamanlı Araç Egzoz Gazı İzleme





![ss](https://user-images.githubusercontent.com/30519822/78463017-c51d3900-76e0-11ea-8a58-d6dc4cd501b3.png)

> Çalışma Mantığı

* Arduino mq2 mq135 ds18b20 sensörlerinden verileri okur. Orange pi Zero (armbian) serial porttan gelen verileri okur ve post eder.
* Django bu isteği ve json verilerini  veritabanına yazar
* Signals veritabanında yeni bir queryset oluştuğu zaman  kaydedilen veriyi  notifications kanalına gönderir
* websocket dinlediği kanaldan yeni veri geldikçe js yardımıyla bunları grafiğe döker




## Kurulum Server

- git clone https://github.com/erelbi/django_websocket_restapi_example.git
- cd django_websocket_restapi_example
- python3.6 kullanıyorsanız #source venv/bin/active
- yeni bir virtualenv oluşturacaksanız #virtualenv 
- #source venv/bin/active
- server kısmı için gerekli paketler
- pip3 install -r requirements.txt
- son olarak sistem redis-server ihtiyaç duymaktadır.
- sudo apt-get install redis
- sudo yum install redis
-  başlatmak için # redis-server
- django başlatmak için # python3 manage.py runserver 0:8000

## Kurulum Arduino
```
#include <OneWire.h>
#include <DallasTemperature.h>
#include <ArduinoJson.h>
#include <MQ2.h>
#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

int val=0;
int Analog_Input = A0;
int lpg, co, smoke;

MQ2 mq2(Analog_Input);
void setup(void)
{
 // start serial port
 Serial.begin(9600);
 Serial.println("Dallas Temperature IC Control Library Demo");
 // Start up the library
 sensors.begin();
 mq2.begin();
}
void loop(void)
{
 float* values= mq2.read(true);
 DynamicJsonBuffer jsonBuffer;
 JsonObject& root = jsonBuffer.createObject();


 sensors.requestTemperatures(); // Send the command to get temperature readings
 val=analogRead(4);//Read Gas value from analog 0
 root["temp"] = sensors.getTempCByIndex(0);
 root["air"] = val,DEC;
 root["co"] = mq2.readCO();
 root["lpg"]= mq2.readLPG();
 root["smoke"]= mq2.readSmoke();
 root.printTo(Serial);
 Serial.println();
 delay(500);
}

```
## Kurulum Arduino
```
import time
import requests
import serial
from threading import Thread
import json


class Sensors():

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.run()

    def run(self):
        while True:
            ser = serial.Serial('/dev/ttyUSB0', 9600)
            data = ser.readline()
#            print(type(data))
            try:
               if json.loads(data):
                  import time
import requests
import serial
from threading import Thread
import json


class Sensors():

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.run()

    def run(self):
        while True:
            ser = serial.Serial('/dev/ttyUSB0', 9600)
            data = ser.readline()
            try:
               if json.loads(data):
                  json_data = print(json.loads(data))
                  air = json_data['air']
                  temp= json_data['temp']
                  lpg = json_data['lpg']
                  smoke = json_data['smoke']
                  co = json_data['co']
                  task = {"air": air, "temp": temp,"lpg":lpg,"smoke":smoke,"co":co}
                  resp = requests.post('http://192.168.43.192:8080/sensorA/', json=task)
            except:
              pass


           if resp.status_code != 201:
               print("error")


Sensors()


```



## Lisans

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://deney.site" target="_blank">deney.site</a>.
# gazi_gomulu_proje
# A-Real-Time-Vehicle-Exhaust-Gas-Monitoring
