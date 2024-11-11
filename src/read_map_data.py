import os
import yaml
# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.rooms import Room

def get_rooms():
    map_file_path = os.path.join("bin", "map_data", "map1.yaml")
    with open(map_file_path, 'r') as map_file:
        room_data = yaml.load(map_file, Loader=yaml.SafeLoader)
    rooms = {}
    for room in room_data['rooms']:
        name = room['name']
        description = room['description']
        rooms[name] = Room(name, description)
    return rooms