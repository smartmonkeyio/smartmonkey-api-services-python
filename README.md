Python Client for SmartMonkey Services
====================================

## Requirements

 - Python 2.7 or later.
 - A SmartMonkey API key.

## Installation

    $ pip install -U smartmonkey

### Install from sources

    $ git clone https://github.com/smartmonkeyio/smartmonkey-api-services-python.git
    $ cd smartmonkey-api-services-python
    $ python setup.py install
    
## Developer Documentation

View the [reference documentation](https://smartmonkeyio.github.io/smartmonkey-api-services-python)

## Usage

This example optimizes a route with one vehicle and two stops:

```python
from smartmonkey.client import (Client)

# Define the vehicles
vehicles = [{
    'id': 'My Fancy Vehicle',
    'start': {'lat': 1.23, 'lng': 1.42},
    'end': {'lat': 1.24, 'lng': 1.42},
    'capacity': [20],
    'timewindow': [36000, 68400],
    'provides': ['candy', 'sushi']
}]

# Define the services
services = [{
    'id': 'Candy shop',
    'location': {'lat': 1.234, 'lng': 4.324},
    'size': [1],
    'capacity': [14],
    'timewindows': [[36000, 68400]],
    'duration': 3600,
    'reward': 100,
    'optional': False,
    'requires': ['candy'],
},
{
    'id': 'Sushi shop',
    'location': {'lat': 2.234, 'lng': 8.324},
    'size': [1],
    'capacity': [14],
    'timewindows': [[36000, 68400]],
    'duration': 3600,
    'reward': 50,
    'optional': False,
    'requires': ['sushi'],
}]

# Setup client: You NEED to set the key in the following line
api_client = Client(key='INSERT_YOUR_API_KEY_HERE')

# Start optimization
optimized_route = api_client.optimize(vehicles, services, synchronous=True)

# Print optimized route
print(optimized_route)
```

## Building the Project

```bash

python setup.py sdist bdist_wheel
twine upload dist/*

```

Generate documentation

```bash

sphinx-build -a -E -b html -d docs/_build/doctrees docs docs/_build/html

```
