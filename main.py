from src.read_map_data import get_rooms

rooms = get_rooms()
current_room = rooms['Entrance Hall']

while True:
    print(f'Current Room: {current_room.name}')
    command = input('Input your command: ')
    print(f'You input {command}')
    print(f'Moving north...')
    current_room = current_room.exits['north'].destination

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