class Item():
    def __init__(self, name, description, value, weight):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
        self.type = self.__class__.__name__.lower()

class Weapon(Item):
    def __init__(self, name, description, value, weight, damage, durability):
        super().__init__(name, description, value, weight)
        self.damage = damage
        self.durability = durability

class Armor(Item):
    def __init__(self, name, description, value, weight, defense_rating, durability):
        super().__init__(name, description, value, weight)
        self.defense_rating = defense_rating
        self.durability = durability

class Tool(Item):
    def __init__(self, name, description, value, weight, usage_count):
        super().__init__(name, description, value, weight)
        self.usage_count = usage_count

class Consumable(Item):
    def __init__(self, name, description, value, weight, effect, amount):
        super().__init__(name, description, value, weight)
        self.effect = effect
        self.amount = amount

class Light(Item):
    def __init__(self, name, description, value, weight, duration_turns, state='off'):
        super().__init__(name, description, value, weight)
        self.duration = duration_turns
        self.state = state

class KeyItem(Item):
    def __init__(self, name, description, value, weight, purpose):
        super().__init__(name, description, value, weight)
        self.purpose = purpose

class Bag(Item):
    def __init__(self, name, description, value, weight, capacity, inventory):
        super().__init__(name, description, value, weight)
        self.capacity = capacity
        self.inventory = {}
        for item in inventory:
            self.inventory[item] = inventory[item]

class MagicItem(Item):
    def __init__(self, name, description, value, weight, effect, charges_remaining):
        super().__init__(name, description, value, weight)
        self.effect = effect
        self.charges_remaining = charges_remaining

class WorldItem():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.type = self.__class__.__name__.lower()

class Container(WorldItem):
    def __init__(self, name, description, inventory, capacity, is_locked):
        super().__init__(name, description)
        self.is_locked = is_locked
        self.capacity = capacity
        self.inventory = {}
        for item in inventory:
            self.inventory[item] = inventory[item]

class Trap(WorldItem):
    def __init__(self, name, description, condition, damage):
        super().__init__(name, description)
        self.condition = condition
        self.damage = damage

class Door(WorldItem):
    def __init__(self, name, description, condition, exit_direction, is_locked):
        super().__init__(name, description)
        self.condition = condition
        self.exit_direction = exit_direction
        self.is_locked = is_locked

if __name__ == '__main__':
    pass