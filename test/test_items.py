import sys, os
import unittest
import src.items as items

# run `python3 -m unittest test.test_items`
# from the commandline at the project root

class TestItemClasses(unittest.TestCase):

    def test_weapon_creation(self):
        sword = items.Weapon('Sword', 'a simple roman cavalry sword', 50, 20, 10, 15)
        self.assertEqual(sword.name, 'Sword')
        self.assertEqual(sword.description, 'a simple roman cavalry sword')
        self.assertEqual(sword.value, 50)
        self.assertEqual(sword.weight, 20)
        self.assertEqual(sword.damage, 10)
        self.assertEqual(sword.durability, 15)
        self.assertEqual(sword.type, 'weapon')

    def test_armor_creation(self):
        armor = items.Armor('Plate Armor', 'a sturdy plate armor', 100, 30, 50, 40)
        self.assertEqual(armor.name, 'Plate Armor')
        self.assertEqual(armor.description, 'a sturdy plate armor')
        self.assertEqual(armor.value, 100)
        self.assertEqual(armor.weight, 30)
        self.assertEqual(armor.defense_rating, 50)
        self.assertEqual(armor.durability, 40)
        self.assertEqual(armor.type, 'armor')

    def test_tool_creation(self):
        hammer = items.Tool('Hammer', 'a heavy steel hammer', 25, 10, 50)
        self.assertEqual(hammer.name, 'Hammer')
        self.assertEqual(hammer.description, 'a heavy steel hammer')
        self.assertEqual(hammer.value, 25)
        self.assertEqual(hammer.weight, 10)
        self.assertEqual(hammer.usage_count, 50)
        self.assertEqual(hammer.type, 'tool')

    def test_consumable_creation(self):
        health_potion = items.Consumable('Health Potion', 'restores health', 5, 1, 'health', 50)
        self.assertEqual(health_potion.name, 'Health Potion')
        self.assertEqual(health_potion.description, 'restores health')
        self.assertEqual(health_potion.value, 5)
        self.assertEqual(health_potion.weight, 1)
        self.assertEqual(health_potion.effect, 'health')
        self.assertEqual(health_potion.amount, 50)
        self.assertEqual(health_potion.type, 'consumable')

    def test_light_creation(self):
        flashlight = items.Light('Flashlight', 'a powerful flashlight', 10, 2, 100)
        self.assertEqual(flashlight.name, 'Flashlight')
        self.assertEqual(flashlight.description, 'a powerful flashlight')
        self.assertEqual(flashlight.value, 10)
        self.assertEqual(flashlight.weight, 2)
        self.assertEqual(flashlight.duration, 100)
        self.assertEqual(flashlight.state, 'off')
        self.assertEqual(flashlight.type, 'light') 

    def test_keyitem_creation(self):
        skeleton_key = items.KeyItem('Skeleton Key', 'a key for many locks', 15, 0.2, 'unlock doors')
        self.assertEqual(skeleton_key.name, 'Skeleton Key')
        self.assertEqual(skeleton_key.description, 'a key for many locks')
        self.assertEqual(skeleton_key.value, 15)
        self.assertEqual(skeleton_key.weight, 0.2)
        self.assertEqual(skeleton_key.purpose, 'unlock doors')
        self.assertEqual(skeleton_key.type, 'keyitem')

    def test_bag_creation(self):
        bag = items.Bag('Leather Bag', 'a small leather bag', 10, 1, 5, {'item1': 2, 'item2': 3})
        self.assertEqual(bag.name, 'Leather Bag')
        self.assertEqual(bag.description, 'a small leather bag')
        self.assertEqual(bag.value, 10)
        self.assertEqual(bag.weight, 1)
        self.assertEqual(bag.capacity, 5)
        self.assertEqual(bag.inventory, {'item1': 2, 'item2': 3})
        self.assertEqual(bag.inventory['item1'], 2)
        self.assertEqual(bag.type, 'bag') 

    def test_magicitem_creation(self):
        magic_staff = items.MagicItem('Magic Staff', 'a staff with magical powers', 50, 5, 'fireball', 3)
        self.assertEqual(magic_staff.name, 'Magic Staff')
        self.assertEqual(magic_staff.description, 'a staff with magical powers')
        self.assertEqual(magic_staff.value, 50)
        self.assertEqual(magic_staff.weight, 5)
        self.assertEqual(magic_staff.effect, 'fireball')
        self.assertEqual(magic_staff.charges_remaining, 3)
        self.assertEqual(magic_staff.type, 'magicitem')

    def test_container_creation(self):
        chest = items.Container('Wooden Chest', 'a sturdy wooden chest', {'gold': 100}, 10, True)
        self.assertEqual(chest.name, 'Wooden Chest')
        self.assertEqual(chest.description, 'a sturdy wooden chest')
        self.assertEqual(chest.inventory, {'gold': 100})
        self.assertEqual(chest.inventory['gold'], 100)
        self.assertEqual(chest.capacity, 10)
        self.assertEqual(chest.is_locked, True)
        self.assertEqual(chest.type, 'container')

    def test_trap_creation(self):
        spike_trap = items.Trap('Spike Trap', 'a trap with sharp spikes', 'triggered', 50)
        self.assertEqual(spike_trap.name, 'Spike Trap')
        self.assertEqual(spike_trap.description, 'a trap with sharp spikes')
        self.assertEqual(spike_trap.condition, 'triggered')
        self.assertEqual(spike_trap.damage, 50)
        self.assertEqual(spike_trap.type, 'trap')

    def test_door_creation(self):
        wooden_door = items.Door('Wooden Door', 'a solid wooden door', 'closed', 'north-east', False)
        self.assertEqual(wooden_door.name, 'Wooden Door')
        self.assertEqual(wooden_door.description, 'a solid wooden door')
        self.assertEqual(wooden_door.condition, 'closed')
        self.assertEqual(wooden_door.exit_direction, 'north-east')
        self.assertEqual(wooden_door.is_locked, False)
        self.assertEqual(wooden_door.type, 'door')