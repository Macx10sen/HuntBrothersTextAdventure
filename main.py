from src.read_map_data import get_rooms
from src.cmds import input_parsing
from src.player import Player
print(f'\nHunt Brothers Text Adventures Presents:\nEscape Room!')
player_name = input(f'\nWelcome to the Escape Room! Please enter your name.\n--> ')
print()

player = Player(player_name)
player.current_room = get_rooms()

player.display_room() #display room before beginning loop, comment this line to put in loop

while True:
#    player.display_room() #comment this line to remove from loop
    command = input('\n--> ')
    input_parsing(player, command)

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