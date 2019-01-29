from smartmonkey import Client

# Request SmartMonkey API key. Can be obtained at: https://flake.smartmonkey.io
api_key = raw_input("* Type your api key: ")
client = Client(api_key)

# Create one vehicle
vehicles = [
    {
        "id": str("Car"),
        "start": {'lat': 41.387617, 'lng': 2.169132},
        "end": {'lat': 41.380739, 'lng': 2.122924}
    }
]

# Provide service descriptions
services = [
    {
        "id": 'Parc Guell',
        "location": {'lat': 41.413262, 'lng': 2.152945},
        "duration": 3600
    },
    {
        "id": 'Sagrada Familia',
        "location": {'lat': 41.403378, 'lng': 2.173600},
        "duration": 3600
    },
    {
        "id": 'Arc de triomf',
        "location": {'lat': 41.391485, 'lng': 2.180159},
        "duration": 3600
    }
]

# Optimize route
optimized_route = client.optimize(vehicles, services)

# Print result
print(optimized_route)