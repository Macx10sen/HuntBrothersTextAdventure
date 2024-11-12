#rooms

class Room: #create Room class
  def __init__(self, name, description, exits): #define room
    self.name = name
    self.description = description
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
