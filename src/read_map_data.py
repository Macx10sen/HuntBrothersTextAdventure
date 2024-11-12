import os, sys
import yaml
# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def get_rooms():
    map_file_path = os.path.join("bin", "map_data", "map1.yaml")
    with open(map_file_path, 'r') as map_file:
        map_data = yaml.load(map_file, Loader=yaml.SafeLoader)
        room_data = map_data['rooms']
    rooms = {}
    for room in room_data:
        name = room['name']
        description = room['description']
        exits = room['exits']
        rooms[name] = Room(name, description, exits)
        # rooms[name].get_exits(connection_data)
    return rooms

if __name__ == '__main__':
    from rooms import Room
    get_rooms()

else:
    from .rooms import Room
