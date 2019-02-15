from smartmonkey.models import CallbackConfiguration
from smartmonkey.models import OptimizeQuery
from smartmonkey.models import ResultQuery
from smartmonkey.models import RewardRegion
from smartmonkey.models import Service
from smartmonkey.models import Vehicle


def optimize(
    client, vehicles, services, reward_region=[],
    synchronous=True, callback=None,
):
    """Launch a Smartmonkey route optimization given a list
    of vehicles and services.

    This example provides two services and one vehicle to
    the optimization::

        vehicles = [
            {
                "id": "Tesla 1",
                "start": {
                    "lat": 4.13,
                    "lng": 20.18,
                },
                "end": {
                    "lat": 4.23,
                    "lng": 19.85,
                },
                "capacity": [20],
                "timewindow": [36000, 120400],
                "provides": ["candy", "marshmallows"]
            }
        ]

        services = [
            {
                "id": "Provide Candy",
                "location": {"lat": 41.45, "lng": 2.14},
                "size": [1],
                "capacity": [10],
                "timewindows": [[36000, 68400]],
                "duration": 3600,
                "reward": 100,
                "optional": False,
                "pickups": {
                    "id": "Pickup candy",
                    "location": {
                        "lat": 41.345,
                        "lng": 2.15623
                    }
                }
            },
            {
                "id": "Provide Marshmallows",
                "location": {"lat": 41.35, "lng": 2.14},
                "size": [1],
                "capacity": [10],
                "timewindows": [[50000, 120400]],
                "duration": 3600,
                "reward": 100,
                "optional": False,
                "requires": ["marsmallows"],
            },
        ]

    **Synchronous response**

    Now just create the client and launch the optimization function.
    By default the result is synchronous, so the function will end as
    soon as the server finish the process::

        from smartmonkey import Client

        api_client = Client(key=MY_API_CLIENT_KEY)
        result = api_client.optimize(vehicles, services)

    **Asynchronous response**

    Sometimes, one might want to get the result asynchronously. In
    that case is possible to set the parameter synchronous to **False**.
    The response of the server will contain a *job_id* parameter with
    which we'll be able to check the results later::

        result = api_client.optimize(
            vehicles,
            services,
            synchronous=False
        )
        print(result['job_id'])

    **Asynchronous response with callback**

    The third way to get the results is specifying a callback url
    so once the server finish the optimization, the result will be
    sent to that url::

        result = api_client.optimize(
            vehicles,
            services,
            synchronous=False
            callback="http://example.com/"
        )

    :param vehicles: A list of dictionaries representing a vehicle.
        Each vehicle must contain Vehicle Model properties.
    :type vehicles: list

    :param services: A list of dictionaries representing a service.
        Each service must contain Service Model properties
    :type services: list

    :param reward_region: A list of dictionaries with all the reward
        regions, must contain 'lat', 'lng', 'radius', and 'reward'.
    :type reward_region: list

    :param synchronous: *(default True)* If synchronous is set to True,
        the request will still alive until the optimization ends. If set
        to false it will return a job id.
    :type synchronous: bool

    :param callback: *(default None)* If synchronous is False is
        possible to set a callback url where the results will be placed
        once the optimization is finished.
    :type callback: string
    """
    if type(vehicles) != list or len(vehicles) < 1:
        raise Exception(
            "`vehicles` should be a list with at least one vehicle.",
        )
    if type(services) != list or len(services) < 1:
        raise Exception(
            "`services` should be a list with at least one service.",
        )
    if type(reward_region) != list:
        raise Exception("`reward_region` should be a list.")

    vehicles_s = [Vehicle(vehicle) for vehicle in vehicles]
    services_s = [Service(service) for service in services]
    reward_region_s = [RewardRegion(rr) for rr in reward_region]
    configuration = CallbackConfiguration({
        "wait": synchronous,
        "callback": callback,
    })

    query = OptimizeQuery(
        vehicles_s, services_s,
        reward_region_s, configuration,
    )
    return client._request(query)


def get_results(client, job_id):
    """Get the result of an optimization given a job id

    :param job_id: The job id of one optimization. This parameter is returned
        when an optimization process start. Is it possible to retrieve past
        optimizations with the id.
    :type job_id: string
    """
    query = ResultQuery({"job_id": job_id})
    return client._request(query)
