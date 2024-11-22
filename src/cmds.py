import sys

def move(player, cmd):
    if cmd in direction_syns:
        direction = direction_syns[cmd]
    else: 
        print("Why would you want to go that way?")
        return
    new_room, error_message = player.current_room.move(player, direction)
    if new_room == None:
        print(error_message)
    else:
        player.current_room = new_room
        player.display_room()

def unlock(player, cmd):
    if cmd != 'door':
        print('What would you like to unlock?')
        return

    locked_exits = []
    for exit in player.get_exits():
        if player.is_locked(exit):
            locked_exits.append(exit)

    if len(locked_exits) == 0:
        status_message = 'Dude... nothing is locked...'
    if len(locked_exits) > 2:
        unlock_options = ', '.join(locked_exits[:-1])
        unlock_options += f', or {locked_exits[-1]}' 
        unlock_options += '.'
        print(f'There are locked doors to the {unlock_options}')
    elif len(locked_exits) > 1:
        unlock_options = ' or '.join(locked_exits)
        unlock_options += '.'
        print(f'There are locked doors to the {unlock_options}')
        status_message = f'Which way would you like to go?'
    else:
        print(f'There is a locked door to the {locked_exits[0]}')
        status_message = player.current_room.unlock(player, locked_exits[0])

    print(status_message)

def check(player, cmd):
    if cmd in inventory_syn: 
        print(player.display_inv())
    elif cmd in room_syn:
        player.display_room()

def grab(player, item):
    player.add_to_inv(item)

def exit():
    exit_confirmation = input('Type yes to confirm: ').lower()
    if exit_confirmation in yes_syn: 
        sys.exit(0)



#cmd synonyms -- add to or change these as needed
move_syn = ["move", "m", "go", 'g', "travel", "walk", "run"]
check_syn = ["check", "c"]
help_syn = ["help", "h"]
grab_syn = ["grab", "obtain", "pick", "take"] #pick?
exit_syn = ['exit']
yes_syn = ['yes', 'y']
inventory_syn = ['inventory', 'i']
room_syn = ['room', 'r']
unlock_syn = ['unlock']

direction_syns = {
    'north': 'north',
    'n': 'north',
    'east': 'east',
    'e': 'east',
    'south': 'south',
    's': 'south',
    'west': 'west',
    'w': 'west',

    'northeast': 'northeast',
    'ne': 'northeast',
    'northwest': 'northwest',
    'nw': 'northwest',
    'southeast': 'southeast',
    'se': 'southeast',
    'southwest': 'southwest',
    'sw': 'southwest',

    'up': 'up',
    'u': 'up',
    'down': 'down',
    'd': 'down',
}


#cmd list

'''Cmds = ["move [direction]", "Check [Stat]", "Grab [item]", "Store [item]", "Eat [item]", "help", "help [cmd]" ]  
     #Move Options: North, East, South, West; Depending on what room the character is located in. Use "help move" to see options
     #Check Options: Health, Hunger?, Inventory (inventory sub types?). Use "help check" to see options
     #Grab Options: Limited by items in the room the character is located in. Use "help grab" to see options
     #Store Options: Limited by items currently in the characters hands. Use "help store" to see options. Also "Check Inventory Hands"?
     #Eat Options: Limited by food items in hand. use for hunger bar? or health regen? Item Subtype?
     #help shortcuts, help shortcuts[cmd]? show acceptable shorthand for various commands? specific commands? both?'''


def input_parsing(player,cmd):
#    cmd_list = [
#        {move_syn:  move()},
#        {check_syn: check()},
#        {grab_syn:  grab()}
#    ]
    cmd = cmd.lower().split()
    primary_cmd = cmd[0]
    secondary_cmds = cmd[1:]
    if primary_cmd in move_syn:
        move(player, secondary_cmds[0])
    elif primary_cmd in direction_syns:
        move(player, primary_cmd)
    elif primary_cmd in check_syn:
        check(player, secondary_cmds[0])
    elif primary_cmd in grab_syn:
        grab(player, secondary_cmds[0])
    elif primary_cmd in exit_syn:
        exit()
    elif primary_cmd in unlock_syn:
        if len(secondary_cmds) == 0:
            secondary_cmds = ['']
        unlock(player, secondary_cmds[0])
    else:
        print(f"{player.name}, that is not a valid command. Please try again.")

'''
move - go, walk, run, head

commands = {'move': move, 
            'go':   'move', 
            'walk': 'move'}
if cmd in commands.keys():
    commands['go']()
'''
