import os, sys
import yaml

# reading rooms as a tree structure
# TODO: check if any of the room connections are already in the tree,
#       else, start new tree
#       eventually the trees should merge into one

def get_rooms():
    map_file_path = os.path.join("bin", "map_data", "map1.yaml")
    with open(map_file_path, 'r') as map_file:
        map_data = yaml.load(map_file, Loader=yaml.SafeLoader)
    root = None
    rooms = {}
    for room_name, room_data in map_data.items():
        description = room_data['description']
        room_object = Room(room_name, description)
        if root == None:
            root =  room_object
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

    return root

if __name__ == '__main__':
    from rooms import Room, Exit
    get_rooms()

else:
    from .rooms import Room, Exit
