#rooms

class Room: #create Room class
  def __init__(self, name, description): #define room
    self.name = name
    self.description = description
    self.exits = {}

  def output(self):
    print(f'{self.name}')
    output = ''
    output = f'You are in the {self.name}. When you look around you see {self.description} '
    for exit_direction in self.exits:
      output += f'You see {self.get_exit_description(exit_direction)} to the {exit_direction}. '
    print(f'{output}')

  def get_exit_description(self, direction):
    return self.exits[direction].description

  def add_exit(self, direction, exit):
    self.exits[direction] = exit

  def move(self, player, direction):
    error_message = ''
    new_room = None
    if direction in self.exits:
      if not self.is_locked(direction):
        new_room = self.get_destination(direction)
      else:
        if self.get_password(direction):
          new_room = self.get_destination(direction)
        else:
          error_message = f"That's the wrong password, {player.name}... idiot."
    else: 
      error_message = "You can't go there."
    return (new_room, error_message)

  def get_password(self, direction):
    input_password = input('That way is locked. Please enter password:\n--> ')
    actual_password = self.exits[direction].password
    return input_password == actual_password

  def is_locked(self, direction):
    return self.exits[direction].locked

  def get_destination(self, direction):
    return self.exits[direction].destination

class Exit:
  def __init__(self, direction, destination_name, description, locked, password=''):
    self.direction = direction
    self.destination = None
    self.destination_name = destination_name
    self.description = description
    self.locked = locked
    self.password = password

  def add_destination(self, destination):
    self.destination = destination