#rooms

class Room: #create Room class
  def __init__(self, name, description): #define room
    self.name = name
    self.description = description
    self.exits = {}

  def add_exit(self, direction, exit):
    self.exits[direction] = exit

  def move(self, direction):
    if direction in self.exits:
      return self.exits[direction].destination
    return None

class Exit:
  def __init__(self, direction, destination_name, description, locked):
    self.direction = direction
    self.destination = None
    self.destination_name = destination_name
    self.description = description
    self.locked = locked

  def add_destination(self, destination):
    self.destination = destination