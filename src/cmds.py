#all commands will be in this file

def move(player, cmd):
    new_room, error_message = player.current_room.move(cmd)
    if new_room == None:
        print(error_message)
    else:
        player.current_room = new_room
    player.display_room()

def check(player, cmd):
    if cmd == "inventory":
        print(player.display_inv())
    elif cmd == "room":
        player.display_room()

def grab(player, item):
    player.add_to_inv(item)

#cmd synonyms -- add to or change these as needed
move_syn = ["move", "m", "go", "g", "travel", "walk", "run"]
check_syn = ["check", "c"]
help_syn = ["help", "h"]
grab_syn = ["grab", "g", "obtain", "pick"] #pick?

#cmd list

'''Cmds = ["move [direction]", "Check [Stat]", "Grab [item]", "Store [item]", "Eat [item]", "help", "help [cmd]" ]  
     #Move Options     : North, East, South, West; Depending on what room the character is located in. Use "help move" to see options
     #Check Options    : Health, Hunger?, Inventory (inventory sub types?). Use "help check" to see options
     #Grab Options     : Limited by items in the room the character is located in. Use "help grab" to see options
     #Store Options    : Limited by items currently in the characters hands. Use "help store" to see options. Also "Check Inventory Hands"?
     #Eat Options      : Limited by food items in hand. use for hunger bar? or health regen? Item Subtype?
     #help shortcuts, help shortcuts[cmd]? show acceptable shorthand for various commands? specific commands? both?'''


def input_parsing(player,cmd):
#    cmd_list = [
#        {move_syn:  move()},
#        {check_syn: check()},
#        {grab_syn:  grab()}
#    ]
    cmd                     = cmd.lower().split()
    primary_cmd             = cmd[0]
    secondary_cmds          = cmd[1:]
    if primary_cmd in move_syn:
        move(player, secondary_cmds[0])
    elif primary_cmd in check_syn:
        check(player, secondary_cmds[0])
    elif primary_cmd in grab_syn:
        grab(player, secondary_cmds[0])
    else:
        print(f"{player.name}, that is not a valid command. Please try again")

'''
move - go, walk, run, head

commands = {'move': move, 
            'go':   'move', 
            'walk': 'move'}
if cmd in commands.keys():
    commands['go']()
'''