import unittest

from smartmonkey.client import (
    Client,
)
# import responses


class TestOptimize(unittest.TestCase):
    def test_input_parameters(self):
        vehicle1 = {
            "id": "1234",
            "start": {"lat": 1.23, "lng": 1.42},
            "end": {"lat": 1.24, "lng": 1.55},
            "capacity": [
                20,
            ],
            "timewindow": [
                36000,
                68400,
            ],
            "provides": [
                "coal",
                "fuel",
            ],
        }

        service1 = {
            "id": "Candy shops",
            "location": {"lat": 1.234, "lng": 4.324},
            "size": [1],
            "capacity": [14],
            "timewindows": [[36000, 68400]],
            "duration": 3600,
            "reward": 100,
            "optional": True,
            "requires": ["fuel"],
            "pickups": [
                {
                    "id": "mypickup",
                    "location": {
                        "lat": 41.3855048,
                        "lng": 2.161903,
                    },
                    "duration": 10,
                    "timewindows": [[3600, 7200]],
                    "size": [1],
                },
            ],
        }

        api_client = Client(
            key="VWgraHRaYlRackQ0SkFVZGlyZkd1Y3NTUm9JMGdxZ0" +
            "1XcHQ1bEV6QjJLekNrczNiMkZFYW9ZNkRQa2JldEx1ZXUra" +
            "1VYUkJkWGRwR3VQQ2ZjMHFta3c9PQ==",
        )
        res = api_client.optimize([vehicle1], [service1], synchronous=True)
        res = api_client.get_results(res['job_id'])
