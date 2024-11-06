#rooms

class Room: #create Room class
  def __init__(self, name, description, items): #define room
    self.name = name
    self.description = description
    self.exits = {} #dictionary for exits, as the direction defines also the room that the direction will take you to
    self.items = items

  def __str__(self):
    return self.name

  def create_exit(self, direction, NextRoom): #define exit method
    self.exits[direction] = NextRoom

# Create Rooms
# Lobby 		= Room("Lobby","Generic Description that says you can either go north, south, east, or west")
# N_ofLobby	= Room("NorthHall", "Generic Room Description")
# S_ofLobby	= Room("SouthHall", "Generic Room Description")
# W_ofLobby	= Room("WestHall", "Generic Room Description")
# E_ofLobby	= Room("WestHall", "Generic Room Description")

# Create Exits in Rooms
# Lobby.create_exit("north", N_ofLobby)
# Lobby.create_exit("south", S_ofLobby)
# Lobby.create_exit("west", W_ofLobby)
# Lobby.create_exit("east", E_ofLobby)
