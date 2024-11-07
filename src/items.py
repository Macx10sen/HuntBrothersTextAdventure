class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class Weapon(Item):
    def __init__(self, name, description, value, damage, durability):
        super().__init__(name, description, value)
        self.damage = damage
        self.durability = durability
class Armor(Item):
    def __init__(self, name, description, value, defense_rating, durability):
        super().__init__(name, description, value)
        self.defense_rating = defense_rating
        self.durability = durability

class Tool(Item):
    def __init__(self, name, description, value, usage_count):
        super().__init__(name, description, value)
        self.usage_count = usage_count

class Consumable(Item):
    def __init__(self, name, description, value, effect, amount):
        super().__init__(name, description, value)
        self.effect = effect
        self.amount = amount

class Light(Item):
    def __init__(self, name, description, value, brightness, duration):
        super().__init__(name, description, value)
        self.brightness = brightness
        self.duration = duration
        self.state = 'off'  # Can be 'on' or 'off'

class KeyItem(Item):
    def __init__(self, name, description, value, purpose):
        super().__init__(name, description, value)
        self.purpose = purpose

class Bag(Item):
    def __init__(self, name, description, value, capacity):
        super().__init__(name, description, value)
        self.capacity = capacity
        self.contents = []

class MagicItem(Item):
    def __init__(self, name, description, value, effect, charges_remaining):
        super().__init__(name, description, value)
        self.effect = effect
        self.charges_remaining = charges_remaining

class WorldItem(Item):
    def __init__(self, name, description):
        super().__init__(name, description, value=0)

class Container(WorldItem):
    def __init__(self, name, description, is_locked):
        super().__init__(name, description)
        self.is_locked = is_locked
        self.contents = []

class Trap(WorldItem):
    def __init__(self, name, description, condition, damage):
        super().__init__(name, description)
        self.condition = condition
        self.damage = damage

class Door(WorldItem):
    def __init__(self, name, description, condition, is_locked):
        super().__init__(name, description)
        self.condition = condition
        self.is_locked = is_locked