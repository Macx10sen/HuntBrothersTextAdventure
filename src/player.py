#player data

class Player:
    def __init__(self,name):
        self.name            = name
        self.current_room    = None
        self.inventory       = []

    def get_inv(self):
        return self.inventory

    def add_to_inv(self,item):
        self.inventory.append(item)
