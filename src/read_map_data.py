import os, sys
import yaml
# import sys, os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def get_rooms():
    map_file_path = os.path.join("bin", "map_data", "map1.yaml")
    with open(map_file_path, 'r') as map_file:
        map_data = yaml.load(map_file, Loader=yaml.SafeLoader)
    rooms = {}
    for room_name, room_data in map_data.items():
        description = room_data['description']
        room_object = Room(room_name, description)
        rooms[room_name] = room_object
        
        for direction, exit_data in room_data['exits'].items():
            destination_name = exit_data['destination']
            description = exit_data['description']
            locked = exit_data['locked']
            exit_object = Exit(direction, destination_name, description, locked)
            room_object.add_exit(direction, exit_object)

    for room_name, room_data in rooms.items():
        for direction, exit_data in room_data.exits.items():
            exit_data.add_destination(rooms[exit_data.destination_name])

    return rooms

if __name__ == '__main__':
    from rooms import Room, Exit
    get_rooms()

else:
    from .rooms import Room, Exit
