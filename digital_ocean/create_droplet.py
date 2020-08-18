import digital_ocean_api as api
from pprint import pprint
import time
import json
import argparse

DESIRED_SIZE = 'c-4'
pprint(api.list_droplets())

def get_desired_size(desired_size):
    matching_sizes = [size for size in api.list_sizes() if size.slug == desired_size]
    if len(matching_sizes) < 1:
        return None
    return matching_sizes[0]

parser = argparse.ArgumentParser(description='Create a new droplet')
parser.add_argument('--delete_when_done', '-d', help='delete once droplet is active', action='store_true')
args = parser.parse_args()

try:
    size = get_desired_size(DESIRED_SIZE)
    if size is None:
        raise Exception("No instances available with size " + DESIRED_SIZE)

    region = [region for region in size.regions if 'nyc' in region][0]
    print(f"Creating droplet of size {size.slug} with {size.memory / 1000}GB of memory and {size.cpus} cpus in region {region}")
    droplet = api.create_droplet(size, region)
    print(f"Created droplet {droplet.id}")

    total_time = 30
    sleep_duration = 2
    for i in range(int(total_time / sleep_duration)):
        time.sleep(sleep_duration)
        droplet = api.get_droplet(droplet.id)
        if droplet.status == 'new':
            print(f'Droplet {droplet.id} is still new; waiting')
        else:
            print(f'Droplet {droplet.id} is now "{droplet.status}" after {sleep_duration * (i+1)} seconds')
            break
finally:
    if args.delete_when_done:
        print(f"Deleting droplet {droplet.id}")
        api.destroy_droplet(droplet.id)

