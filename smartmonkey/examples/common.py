import json

def print_vehicles(vehicles):
    print(f"")
    print(f"\U0001f698   -> Vehicles:")
    for vehicle in vehicles:
        print(json.dumps(vehicle, sort_keys=True, indent='\t', separators=(',', ': ')))


def print_services(services):
    print(f"")
    print(f"\U0001f4CD   -> Services:")
    for service in services:
        print(json.dumps(service, sort_keys=True, indent='\t', separators=(',', ': ')))

def print_result(result):
    print("")
    print("\U00002705   -> Result:")
    print(json.dumps(result, sort_keys=True, indent='\t', separators=(',', ': ')))

def print_loading():
    print("")
    print("\U0001F504  -> Optimizing...")