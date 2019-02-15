from smartmonkey import Client
from smartmonkey.examples.generators import ServicesGenerator, VehiclesGenerator
from smartmonkey.examples.common import print_vehicles, print_services, print_result, print_loading
import json


if __name__ == "__main__":
    print("====================================================")
    print("\U0001f435   SmartMonkey Optimizer v1: Simple request example")
    print("====================================================")
    API_KEY = input('\U0001f511  -> Input your api key (Or create one https://flake.smartmonkey.io/console/keys): ')
    client = Client(API_KEY)
    print("-> You are going to optimize two services and one vehicle(s):")
    vehicles = VehiclesGenerator(1).data()
    services = ServicesGenerator(2).data()

    print_vehicles(vehicles)
    print_services(services)
    print_loading()

    result = client.optimize(vehicles, services)
    print_result(result)



