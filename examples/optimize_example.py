from smartmonkey import Client
import math
from smartmonkey.models import (
    Vehicle,

)
import threading
import time
import sys
import json


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)



spinner = Spinner()
if __name__ == "__main__":
    print("\n\n")
    print("================== Smartmonkey API Example ==================")
    if (len(sys.argv) == 1):
        print("No API key parameter!")
        print("! you can use `$python optimize_example.py <API_KEY>`")
        api_key = raw_input("* Type your api key: ")
    
    else:
        api_key = sys.argv[1]
    
    print("-- Creating Client" )
    spinner.start()
    client = Client(api_key)
    spinner.stop()
    vehicle_n = raw_input("* Number of vehicles: ")
    services_n = raw_input("* Number of stops: ")

    
    with open('data.json') as f:
        data = json.load(f)
    # vehicles = [
    #     Vehicle({
    #         "id": math.random(),
    #         "start":
    #     }) for x in range(int(vehicle_n))
    # ]



