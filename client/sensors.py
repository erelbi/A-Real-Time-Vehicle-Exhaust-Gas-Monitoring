from time import sleep
import json
import psutil
import requests
from threading import Thread
import random

class A(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            sleep(1)
            temp = random.randint(0,220)
            co = random.randint(0,2000)
            smoke= random.randint(0,800)
            air=random.randint(0,2200)
            lpg=random.randint(0,2000)
            task = {"co":co,  "temp":temp,"smoke":smoke,"air":air,"lpg":lpg}
            resp = requests.post('http://127.0.0.1:8000/sensorA/', json=task)

            if resp.status_code != 201:
                print("error")

A()
while True:
    pass
