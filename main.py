from src.read_map_data import get_rooms

rooms = get_rooms()
current_room = rooms['Entrance Hall']

while True:
    current_room.verbose()
    command = input('Input your command: ')
    print(f'You input {command}')
    current_room = rooms[current_room.exits['north']]