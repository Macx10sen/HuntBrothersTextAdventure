#rooms

class Room: #create Room class
  def __init__(self, name, description): #define room
    self.name = name
    self.description = description
    self.exits = {}

  def add_exit(self, direction, exit):
    self.exits[direction] = exit

  def move(self, direction):
    error_message = ''
    new_room = None
    if direction in self.exits:
      exit = self.exits[direction]
      if not exit.locked:
        new_room = self.exits[direction].destination
      else:
        error_message = 'That way is locked'
    else: 
      error_message = "You can't go there."
    return (new_room, error_message)

class Exit:
  def __init__(self, direction, destination_name, description, locked):
    self.direction = direction
    self.destination = None
    self.destination_name = destination_name
    self.description = description
    self.locked = locked

  def add_destination(self, destination):
    self.destination = destination