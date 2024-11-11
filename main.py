from src.read_map_data import get_rooms

rooms = get_rooms()
print(rooms)

current_room = rooms['Entrance Hall']

while True:
    print(current_room.name)
    print(current_room.description)
    print(current_room.exits)
    command = input('Input your command: ')
    print(f'You input {command}')
    #current_room = rooms[current_room.exits['north']]
    current_room = rooms['Library']

