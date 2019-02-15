from smartmonkey.client import Client
from examples.generators import ServicesGenerator
from examples.generators import VehiclesGenerator

MY_API_CLIENT_KEY = "ZDM3SVhQb0E5SGMzOW94b3RRT1VkNHRKQjV5MTYyM3lTckNCRFNldG5pRitod1hkdjNIZnJKNkYxM24zWWlxdTNMR1YwclhLejJUL1lIVUsxRFA2dVE9PQ=="
api_client = Client(key=MY_API_CLIENT_KEY)

services = ServicesGenerator(50).with_timewindows(
    [[28800, 61200]],
).with_size(10, 0.5).with_duration(360)
vehicles = VehiclesGenerator(5).with_timewindow(
    [28800, 61200],
).with_same_start_end().with_capacity(100, 0.3)

result = api_client.optimize(
    vehicles.data(),
    services.data(),
)
