import requests
import json
from json import JSONEncoder
from pprint import pprint

from models import *
from digital_ocean_auth import get_auth

BASE_URL = "https://api.digitalocean.com"

def list_droplets():
    path = "/v2/droplets"
    return _get(path)


def create_droplet(size: Size, region: str):
    if not size.is_available_in_region(region):
        raise ValueError(f"Cannot create instance of size '{size.slug}' in region '{region}'; it is available in {size.regions}")
    
    payload = {  
        "name": "factorio-server",
        "region": region,
        "size": size.slug,
        "image": "ubuntu-16-04-x64",
        "ssh_keys": [],
        "backups": False,
        "ipv6": False,
        "user_data": None,
        "private_networking": None,
        "volumes": None,
        "tags": [
            "factorio"
        ]
    }
    response = _post("/v2/droplets", payload)
    if response.status_code > 299:
        pprint(response.json())
    response.raise_for_status()

    return Droplet(response.json()['droplet'])

def destroy_droplet(id: str):
    _delete(f"/v2/droplets/{id}")

def get_droplet(id: str):
    payload = _get(f"/v2/droplets/{id}")
    return Droplet(payload['droplet'])

def take_snapshot():
    pass

def delete_snapshot():
    pass

def list_snapshots():
    pass

def list_sizes():
    path = "/v2/sizes"
    return [Size(x) for x in _get(path)["sizes"]]

def to_json(obj):
    return json.dumps(obj, cls=LiberalEncoder)

def _get(path):
    url = BASE_URL + path
    response = requests.get(url, auth=get_auth())
    response.raise_for_status()
    return response.json()

def _post(path, payload):
    url = BASE_URL + path
    response = requests.post(url, payload, auth=get_auth())
    return response

def _delete(path):
    url = BASE_URL + path
    response = requests.delete(url, auth=get_auth())
    if (response.status_code > 299):
        pprint(response.json())
    response.raise_for_status()
    return response

class LiberalEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__  

