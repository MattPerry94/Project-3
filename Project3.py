
import PolyGonAPI
from PolyGonAPI import RESTclient
import json
from typing import cast
from urllib3 import HTTPResponse

clinet = RESTclient(config.API_KEY)

aggs = cast(
    HTTPResponse,
    clinet.get_aggs(
        'AAPL',
        1, 
        'day', 
        '2022-05-20',
        '2022-11-11',
        raw = True
    ),
)

data = json.loads(aggs.data)
print(data)
