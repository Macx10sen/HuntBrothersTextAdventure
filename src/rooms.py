#rooms

class Room: #create Room class
  def __init__(self, name, description, exits): #define room
    self.name = name
    self.description = description
    self.exits = exits

  def __str__(self):
    return self.name