# rooms

class Room:  # create Room class
    def __init__(self, name, description):  # define room
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
                error_message = "The door is locked. It looks like you can type in a password."
        else:
            error_message = "You can't go there."
        return (new_room, error_message)

    def unlock(self, player, direction):
        if direction not in self.exits:
            status_message = "You can't go that way."
            return status_message
        if not self.is_locked(direction):
            status_message = "That way isn't even locked, have you tried turning the doorknob?"
            return status_message
        if not self.correct_password(direction):
            status_message = f"That's the wrong password, {player.name}... idiot."
            return status_message

        # The door is set to unlocked
        self.exits[direction].locked = False
        status_message = "You hear a small click."
        return (status_message)

    def correct_password(self, direction):
        input_password = input('You see a keyboard. Please enter the password:\n--> ')
        actual_password = self.get_password(direction)
        return input_password == actual_password

    def get_password(self, direction):
        return self.exits[direction].password

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
