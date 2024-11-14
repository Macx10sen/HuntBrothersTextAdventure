#all commands will be in this file

#cmd list
Cmds = ["move [direction]", "Check [Stat]", "Grab [item]", "Store [item]", "Eat [item]", "help", "help [cmd]" ]  
     #Move Options     : North, East, South, West; Depending on what room the character is located in. Use "help move" to see options
     #Check Options    : Health, Hunger?, Inventory (inventory sub types?). Use "help check" to see options
     #Grab Options     : Limited by items in the room the character is located in. Use "help grab" to see options
     #Store Options    : Limited by items currently in the characters hands. Use "help store" to see options. Also "Check Inventory Hands"?
     #Eat Options      : Limited by food items in hand. use for hunger bar? or health regen? Item Subtype?
     #help shortcuts, help shortcuts[cmd]? show acceptable shorthand for various commands? specific commands? both?

def input_parsing(current_room,cmd):
    cmd                     = cmd.lower().split()
    primary_cmd             = cmd[0]
    secondary_cmds          = cmd[1:]
    if primary_cmd == "move" or primary_cmd == "m":
        new_room, error_message = current_room.move(secondary_cmds[0])
        if new_room == None:
            print(error_message)
        else:
            return new_room