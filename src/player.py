#player data

class Player:
    def __init__(self,name):
        self.name            = name
        self.current_room    = None
        self.inventory       = []

    def display_inv(self):
        if self.inventory:
            return self.inventory
        else:
            return "Your inventory is empty"

    def add_to_inv(self,item):
        self.inventory.append(item)

    def display_room(self):
        self.current_room.output()

    def get_exits(self):
        return self.current_room.exits

    def get_exit(self, direction):
        return self.current_room.exits[direction]

    def is_locked(self, direction):
        return self.current_room.exits[direction].locked