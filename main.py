from src.read_map_data import get_rooms

current_room = get_rooms()

while True:
    print(f'Current Room: {current_room.name}')
    command = input('Move Direction: ')
    print(f'Moving {command}...')
    new_room, error_message = current_room.move(command)
    if new_room == None:
        print(error_message)
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