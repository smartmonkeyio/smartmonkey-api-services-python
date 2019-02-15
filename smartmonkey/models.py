from smartmonkey.serializer import Serializable


class LatLng(Serializable):
    class Meta:
        schema = {
            "lat": float,
            "lng": float,
        }


class Vehicle(Serializable):
    """

    """
    class Meta:
        schema = {
            "id": str,
            "start?": LatLng,
            "end?": LatLng,
            "capacity?": [float],
            "timewindow?": [int],
            "provides?": [str],
        }


class Pickup(Serializable):
    class Meta:
        schema = {
            "id?": str,
            "location": LatLng,
            "duration?": int,
            "timewindows?": [list],
            "size?": [int],
        }


class Service(Serializable):
    class Meta:
        schema = {
            "id": str,
            "location": LatLng,
            "size?": [int],
            "timewindows?": [list],
            "duration?": int,
            "reward?": float,
            "optional?": bool,
            "requires?": [str],
            "pickups?": [Pickup],
        }


class RewardRegion(Serializable):
    class Meta:
        schema = {
            "lat": float,
            "lng": float,
            "radius": float,
            "reward": float,
        }


class CallbackConfiguration(Serializable):
    class Meta:
        schema = {
            "wait": bool,
            "callback?": str,
        }


class Query:
    def url(self):
        raise NotImplementedError(
            "'url' function must be implemented in all inheriting classes",
        )

    def method(self):
        raise NotImplementedError(
            "'method' function must be implemented " +
            "in all 'inheriting classes'",
        )


class OptimizeQuery(Serializable, Query):
    class Meta:
        schema = {
            "vehicles": [Vehicle],
            "services": [Service],
            "reward_region?": [RewardRegion],
            "configuration": CallbackConfiguration,
        }

    def __init__(self, vehicles, services, reward_region, configuration):
        self.vehicles = vehicles
        self.services = services
        self.reward_region = reward_region
        self.configuration = configuration

    def url(self):
        return '/optimize'

    def method(self):
        return 'POST'


class ResultQuery(Serializable, Query):
    class Meta:
        schema = {
            "job_id": str,
        }

    def url(self):
        return '/optimize'

    def method(self):
        return 'GET'
