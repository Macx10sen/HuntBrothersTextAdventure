from src.read_map_data import get_rooms

current_room = get_rooms()

while True:
    print(f'Current Room: {current_room.name}')
    command = input('Input your command: ')
    print(f'You input {command}')
    print(f'Moving north...')
    new_room = current_room.move('north')
    if new_room == None:
        print("You can't go there.")
    else:
        current_room = new_room

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