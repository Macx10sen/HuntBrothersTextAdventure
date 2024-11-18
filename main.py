from src.read_map_data import get_rooms
from src.cmds import input_parsing
from src.player import Player
print(f'\nHunt Brothers Text Adventures Presents:\nEscape Room!\n')
player_name = input("Welcome to the Escape Room! Please enter your name.")

player = Player(player_name)
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