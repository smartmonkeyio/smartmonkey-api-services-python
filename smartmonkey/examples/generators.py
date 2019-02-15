import random


class RandomGenerator:
    def generate_random_coordinates(self):
        lng_min, lat_min, lng_max, lat_max = - \
            3.8063724716, 40.3553574978, -3.6019447547, 40.4872914853
        lat = random.randrange(
            int(lat_min * 100000),
            int(lat_max * 100000),
        ) / 100000
        lng = random.randrange(
            int(lng_min * 100000),
            int(lng_max * 100000),
        ) / 100000

        return {'lat': lat, 'lng': lng}


class ServicesGenerator(RandomGenerator):
    def __init__(self, n):
        self.services = []
        self._generate_n_services(n)
        self.iter = 0

    def _generate_n_services(self, n):
        for i in range(n):
            service = self._generate_random_service()
            self.services.append(service)
        return self

    def _generate_random_service(self):
        return {
            'id': 'service-' + str(random.randrange(100000, 999999)),
            'location': self.generate_random_coordinates(),
        }

    def with_timewindows(self, timewindows):
        for service in self.services:
            service['timewindows'] = timewindows
        return self

    def with_size(self, size, variability):
        for service in self.services:
            difference = (random.randint(0, variability * 100)) / 100
            difference = size + \
                (random.choice([-1, 1]) * (size * difference))
            service['size'] = [int(difference)]
        return self

    def with_pickups(self, number=None, position=None, mode='different'):
        if mode == 'different':
            if number:
                for i in range(number):
                    pickup = {'location': self.generate_random_coordinates()}
                    self.services[i]['pickups'] = [pickup]
            else:
                for service in self.services:
                    pickup = {'location': self.generate_random_coordinates()}
                    service['pickups'] = [pickup]

        if mode == 'same':
            position = position if position \
                else self.generate_random_coordinates()
            pickup = {'location': position}
            if number:
                for i in range(number):
                    self.services[i]['pickups'] = [pickup]
            else:
                for service in self.services:
                    service['pickups'] = [pickup]

        if mode == 'can-go-back':
            position = position if position \
                else self.generate_random_coordinates()
            position2 = self.generate_random_coordinates()
            for service in self.services:
                pickup = {'location': random.choice([position, position2])}
                service['pickups'] = pickup

        return self

    def with_duration(self, duration):
        for service in self.services:
            service['duration'] = duration
        return self

    def data(self):
        return self.services


class VehiclesGenerator(RandomGenerator):
    def __init__(self, n):
        self.vehicles = self._generate_n_vehicles(n)

    def _generate_random_vehicle(self):
        return {
            "id": 'vehicle-' + str(random.randrange(100000, 999999)),
            "start": self.generate_random_coordinates(),
            "end": self.generate_random_coordinates(),
        }

    def _generate_n_vehicles(self, n):
        vehicles = []
        for i in range(n):
            vehicle = self._generate_random_vehicle()
            vehicles.append(vehicle)
        return vehicles

    def with_timewindow(self, timewindow):
        for vehicle in self.vehicles:
            vehicle['timewindow'] = timewindow
        return self

    def with_same_start_end(self):
        position = self.generate_random_coordinates()
        for vehicle in self.vehicles:
            vehicle['start'] = position
            vehicle['end'] = position
        return self

    def with_capacity(self, capacity, variability):
        for vehicle in self.vehicles:
            difference = (random.randint(0, variability * 100)) / 100
            difference = capacity + \
                (random.choice([-1, 1]) * (capacity * difference))
            vehicle['capacity'] = [int(difference)]
        return self

    def data(self):
        return self.vehicles
