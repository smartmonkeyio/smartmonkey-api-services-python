from smartmonkey import Client
import math
from smartmonkey.models import (
    Vehicle,

)
import threading
import time
import sys
import json
import random


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

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
        sys.stdout.write('\b')
        sys.stdout.flush()
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

    client = Client(api_key)
    vehicle_n = raw_input("* Number of vehicles: ")
    services_n = raw_input("* Number of stops: ")

    with open('addresses.json') as f:
        addresses = json.load(f)['addresses']
        vehicles = [
            {
                "id": str("Vehicle {}".format(i)),
                "start": random.choice(addresses)['coordinate'],
                "end": random.choice(addresses)['coordinate'],
                "capacity": [random.randint(10, 20)]
            } for i in range(int(vehicle_n))
        ]

        services = [
            {
                "id": str("Service {}".format(i)),
                "location": random.choice(addresses)['coordinate'],
                "size": [random.randint(1, 2)],
                "duration": random.randint(5, 15) * 60
            } for i in range(int(services_n))
        ]

        # Start optimization
        print(vehicles)
        print(services)
        spinner.start()
        optimized_route = client.optimize(vehicles, services, synchronous=True)
        spinner.stop()
        # Print optimized route
        print(optimized_route)

