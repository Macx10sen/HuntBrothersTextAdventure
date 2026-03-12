import pytest
from unittest.mock import MagicMock
from src.player import Player


class TestPlayer:
    def test_player_creation(self):
        player = Player("Alice")
        assert player.name == "Alice"
        assert player.current_room is None
        assert player.inventory == []

    def test_empty_inventory(self):
        player = Player("Alice")
        assert player.display_inv() == "Your inventory is empty"

    def test_add_to_inventory(self):
        player = Player("Alice")
        player.add_to_inv("sword")
        player.add_to_inv("key")
        inv = player.display_inv()
        assert "sword" in inv
        assert "key" in inv

    def test_display_room_calls_output(self):
        player = Player("Alice")
        player.current_room = MagicMock()
        player.display_room()
        player.current_room.output.assert_called_once()
