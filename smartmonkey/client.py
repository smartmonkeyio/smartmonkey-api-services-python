import json

import requests

import smartmonkey
from .optimize import get_results
from .optimize import optimize
try:  # Python 3
    from urllib.parse import urlencode
except ImportError:  # Python 2
    from urllib import urlencode  # noqa


_API_VERSION = 'v1'
_USER_AGENT = "SmartmonkeyApiClient/%s" % smartmonkey.__version__
_DEFAULT_BASE_URL = "http://services.smartmonkey.io/api/" + _API_VERSION

_RETRIABLE_STATUSES = {500, 503, 504}


class Client(object):
    """ Performs requests to the Smartmonkey API web services """

    def __init__(self, key, request_kwargs=None):
        """
            :param key: Smartmonkey API Key, this parameter is required.
                This key can be created in https://console.smartmonkey.io
            :type key: string

            :param request_kwargs: Optional headers to include in the http
                request
            :type request_kwargs: dict
        """
        if not key:
            raise ValueError(
                "API Key not provided! Create it in the console or contact" +
                "the administrator.",
            )

        # Create the session params
        self.session = requests.Session()
        self.key = key
        self.request_kwargs = request_kwargs or {}
        self.request_kwargs.update({
            "headers": {"User-Agent": _USER_AGENT},
            "verify": True,  # TODO: Must review this parameter
        })

    def _request(self, query):
        """Function requests recieves a query. It
            :param query: Query containing the parameters, the method and the
                url. It must inherit Query parent class.
            :type query: Query
        """
        url = _DEFAULT_BASE_URL + query.url()
        params = {
            "key": self.key,
        }
        if query.method() == 'POST':
            data = json.dumps(query.write())
            res = requests.post(url, data=data, params=params)

        if query.method() == 'GET':
            params.update(query.write())
            res = requests.get(url, params=params)

        if res.status_code == 200:
            return json.loads(res.content)

        else:
            raise Exception('Network error {}!\n{}'.format(
                res.status_code, res.content,
            ))


# Include the functionalities
Client.optimize = optimize
Client.get_results = get_results
