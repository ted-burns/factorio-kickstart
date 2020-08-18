class Size():

    def __init__(self, response_dict):
        self.slug = response_dict['slug']
        self.regions = response_dict['regions']
        self.hourly_price = response_dict['price_hourly']
        self.disk = response_dict['disk']
        self.memory = response_dict['memory']
        self.transfer = response_dict['transfer']
        self.cpus = response_dict['vcpus']

    def is_available_in_region(self, region: str):
        return region in self.regions

class Region():
    
    def __init__(self, payload):
        self.available = payload["available"]
        self.name = payload['name']
        self.slug = payload['slug']

class Image():

    def __init__(self, payload):
        self.distribution = payload["distribution"]
        self.description = payload["description"]
        self.slug = payload['slug']

class Droplet():

    def __init__(self, payload):
        self.created_at = payload['created_at']
        self.disk_in_gb = payload['disk']
        self.id = payload['id']
        self.locked = payload['locked']
        self.memory_in_gb = payload['memory'] / 1000
        self.name = payload['name']
        self.cpus = payload['vcpus']
        self.snapshot_ids = payload['snapshot_ids']
        self.status = payload['status']
        self.ip_addresses = payload['networks']['v4']
        self.region = Region(payload['region'])
        self.size = Size(payload['size'])
        self.image = Image(payload['image'])
