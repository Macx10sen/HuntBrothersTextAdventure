#rooms

class Room: #create Room class
  def __init__(self, name, description): #define room
    self.name = name
    self.description = description
    self.exits = {}

  def get_exits(self, connections):
    exits = {}
    for connection in connections:
      for room_info in connection['rooms']:
        print(room_info)
      if connection.room1 == self or connection.room2 == self:
        exits[connection.direction_from(self)] = {
          'destination': connection.get_connected_room(self).name,
          'description': connection.description,
          'locked': connection.locked
        }
    self.exits = exits

  def __str__(self):
    return self.name

  def output(self, level='verbose'):
    if level == 'verbose':
      print(f'You are in the {self.name}. ', end='')
      exit_directions = list(self.exits.keys())

      if not exit_directions:
        print('There are no visible exits.')
      elif len(exit_directions) == 1:
        print(f'You see an exit to the {exit_directions[0]}.')
      elif len(exit_directions) == 2:
        print(f'You see exits to the {exit_directions[0]} and {exit_directions[1]}.')
      else:
        print(f'You see exits to the {", ".join(exit_directions[:-1])}, and {exit_directions[-1]}.')

      print(f'When you look around you see {self.description}')

    if level == 'brief':
      print(f'You are in the {self.name}.')

class Connection:
    def __init__(self, room1, room2, direction1, direction2, description, locked=False):
        self.room1 = room1
        self.room2 = room2
        self.direction1 = direction1
        self.direction2 = direction2
        self.description = description
        self.locked = locked

    def direction_from(self, room):
        """Returns the direction to the other room from the given room."""
        return self.direction1 if room == self.room1 else self.direction2

    def get_connected_room(self, room):
        """Returns the opposite room of the one provided."""
        return self.room2 if room == self.room1 else self.room1
