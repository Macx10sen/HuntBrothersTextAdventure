from src.read_map_data import get_rooms
from src.cmds import input_parsing
from src.player import Player
print(f'\nHunt Brothers Text Adventures Presents:\nEscape Room!')
player_name = input(f'\nWelcome to the Escape Room! Please enter your name.\n--> ')

player = Player(player_name)
player.current_room = get_rooms()

while True:
    player.get_room()
    command = input('--> ')
    player.current_room = input_parsing(player.current_room,command)

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