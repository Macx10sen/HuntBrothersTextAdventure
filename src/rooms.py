#rooms

class Room: #create Room class
  def __init__(self, name, description): #define room
    self.name = name
    self.description = description
    self.exits = {}

  def output(self):
    print(f'\n{self.name}')
    output = ''
    output = f'You are in the {self.name}. When you look around you see {self.description} '
    for exit_direction in self.exits:
      output += f'You see {self.get_exit_description(exit_direction)} to the {exit_direction}. '
    print(f'{output}\n')

  def get_exit_description(self, direction):
    return self.exits[direction].description

  def add_exit(self, direction, exit):
    self.exits[direction] = exit

  def move(self, direction):
    error_message = ''
    new_room = None
    if direction in self.exits:
      if not self.is_locked(direction):
        new_room = self.get_destination(direction)
      else:
        error_message = 'That way is locked'
    else: 
      error_message = "You can't go there."
    return (new_room, error_message)

  def is_locked(self, direction):
    return self.exits[direction].locked

  def get_destination(self, direction):
    return self.exits[direction].destination

class Exit:
  def __init__(self, direction, destination_name, description, locked):
    self.direction = direction
    self.destination = None
    self.destination_name = destination_name
    self.description = description
    self.locked = locked

  def add_destination(self, destination):
    self.destination = destination