from src.read_map_data import get_rooms
from src.cmds import input_parsing

current_room = get_rooms()

while True:
    current_room.output()
    command = input('--> ')
    current_room = input_parsing(current_room,command)

'''
gameloop:
    print room 
        name
        description
        exits
        items
    get user input
    process command
'''