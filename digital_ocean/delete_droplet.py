import digital_ocean_api as api
import sys
import argparse
from pprint import pprint
import time

def destroy(droplet_id):
    print(f"Destroying droplet {droplet_id}")
    api.destroy_droplet(droplet_id)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Delete a droplet from digital ocean')
    parser.add_argument('--droplet_id', type=int, help='the id of the droplet to delete', default=-1)
    parser.add_argument('--all', help='deletes all droplets', action='store_true')
    args = parser.parse_args()

    if args.all is not False:
        for droplet_id in [droplet['id'] for droplet in api.list_droplets()['droplets']]:
            destroy(droplet_id)
    elif args.droplet_id > 0:
        destrory(args.droplet_id)
        

    time.sleep(2)
    pprint(api.list_droplets())