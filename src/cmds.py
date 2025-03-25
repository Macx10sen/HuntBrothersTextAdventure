import sys


def move(player, cmd):
    if cmd in direction_syns:
        direction = direction_syns[cmd]
    else:
        print("Why would you want to go that way?")
        return
    new_room, error_message = player.current_room.move(player, direction)
    if new_room is None:
        print(error_message)
    else:
        player.current_room = new_room
        player.display_room()


def unlock(player, cmd):
    if cmd in direction_syns:
        direction = direction_syns[cmd]
    else:
        print("There isn't even a door over there...")
        return
    status_message = player.current_room.unlock(player, direction)
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

#help page
def help(cmd):
    cmd_exists = any(cmd in cmd_syns for cmd_syns in primary_cmd_list)
    if cmd is None:
        print(primary_cmd_list)
    elif cmd_exists:
        if cmd in move_syn:
            help_move()
        elif cmd in check_syn:
            help_check()
        elif cmd in grab_syn:
            help_grab()
        elif cmd in unlock_syn:
            help_unlock()
    else:
        print("That is not a valid command, Please try again")

def learn(cmd):
    cmd_exists = any(cmd in cmd_syns for cmd_syns in primary_cmd_list)
    if cmd is None:
        print("Use the learn command to learn what different commands do. Type 'learn' followed by the command you would like to learn")
    elif cmd_exists:
        if cmd in move_syn:
            learn_move()
        elif cmd in check_syn:
            learn_check()
        elif cmd in grab_syn:
            learn_grab()
        elif cmd in unlock_syn:
            learn_unlock()
    else: 
        print("That command does not exist, Please try again")
        


def learn_move():
    print("The move command is how you move from room to room.")
    print("Type a valid move command followed by the\ndirection of the room you want to travel")
   
def help_move():
    print(f"Acceptable move synonyms are {move_syn}")
    print(f"Acceptable direction synonyms are {direction_syns}")

def learn_check():
    print("The check command can be used to check the status of\nyour players location or inventory")

def help_check():
    print(f"Acceptable check synonyms are {check_syn}")
    print(f"Acceptable secondary commands and appropriate synonyms are\n{inventory_syn} and {room_syn}")

def learn_grab():
    print("The grab command is used to obtain.\nThis command is limited by the items in the same room as your player")

def help_grab():
    print(f"Acceptable grab synonyms are {grab_syn}")

def learn_unlock():
    print("The Unlock command is used to unlock a door in the room you player is located.\nThe direction is limited by the available exits in the room and whether they are locked")

def help_unlock():
    print(f"Acceptable unlock synonyms are {unlock_syn}")
        
        



#cmd synonyms -- add to or change these as needed

#primary cmds
move_syn = ["move", "m", "go", 'g' "travel", "walk", "run", "to"]
check_syn = ["check", "c"]
grab_syn = ["grab", "obtain", "pick", "take"] 
unlock_syn = ['unlock', 'u', 'open', 'o']
exit_syn = ['exit']
yes_syn = ['yes', 'y']
learn_syn = ["learn", "l"]
help_syn = ["help", "h"]

#secondary cmds
inventory_syn = ['inventory', 'i']
room_syn = ['room', 'r','location','l']
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


# cmd list

primary_cmd_list = [
    move_syn,#
    check_syn,#
    grab_syn,#
    unlock_syn,#
    exit_syn,
    learn_syn,
    help_syn,
    ]
'''Cmds = ["move [direction]", "Check [Stat]", "Grab [item]", "Store [item]", "Eat [item]", "help", "help [cmd]" ] 
     #Move Options: North, East, South, West; Depending on what room the character is located in. Use "help move" to see options
     #Check Options: Health, Hunger?, Inventory (inventory sub types?). Use "help check" to see options
     #Grab Options: Limited by items in the room the character is located in. Use "help grab" to see options
     #Store Options: Limited by items currently in the characters hands. Use "help store" to see options. Also "Check Inventory Hands"?
     #Eat Options: Limited by food items in hand. use for hunger bar? or health regen? Item Subtype?
     #help shortcuts, help shortcuts[cmd]? show acceptable shorthand for various commands? specific commands? both?'''


def input_parsing(player,cmd):

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
        unlock(player, secondary_cmds[0])
    elif primary_cmd in help_syn:
        help(secondary_cmds[0])
    elif primary_cmd in learn_syn:
        learn(secondary_cmds[0])
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
