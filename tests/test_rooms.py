import pytest
from unittest.mock import patch
from src.rooms import Room, Exit
from src.player import Player


@pytest.fixture
def empty_room():
    return Room("Test Room", "a plain room")


@pytest.fixture
def two_rooms():
    room_a = Room("Room A", "the first room")
    room_b = Room("Room B", "the second room")
    exit_ab = Exit("north", "Room B", "an archway", locked=False)
    exit_ab.add_destination(room_b)
    room_a.add_exit("north", exit_ab)
    return room_a, room_b


@pytest.fixture
def locked_rooms():
    room_a = Room("Room A", "the first room")
    room_b = Room("Room B", "the second room")
    exit_ab = Exit("north", "Room B", "a locked door", locked=True, password="secret")
    exit_ab.add_destination(room_b)
    room_a.add_exit("north", exit_ab)
    return room_a, room_b


class TestRoom:
    def test_room_creation(self, empty_room):
        assert empty_room.name == "Test Room"
        assert empty_room.description == "a plain room"
        assert empty_room.exits == {}

    def test_add_exit(self, two_rooms):
        room_a, _ = two_rooms
        assert "north" in room_a.exits

    def test_move_valid_unlocked(self, two_rooms):
        room_a, room_b = two_rooms
        new_room, error = room_a.move(None, "north")
        assert new_room is room_b
        assert error == ""

    def test_move_invalid_direction(self, empty_room):
        new_room, error = empty_room.move(None, "north")
        assert new_room is None
        assert error == "You can't go there."

    def test_move_locked_door(self, locked_rooms):
        room_a, _ = locked_rooms
        new_room, error = room_a.move(None, "north")
        assert new_room is None
        assert "locked" in error.lower()

    def test_unlock_invalid_direction(self, empty_room):
        player = Player("Tester")
        player.current_room = empty_room
        result = empty_room.unlock(player, "north")
        assert result == "You can't go that way."

    def test_unlock_already_unlocked(self, two_rooms):
        room_a, _ = two_rooms
        player = Player("Tester")
        player.current_room = room_a
        result = room_a.unlock(player, "north")
        assert "isn't even locked" in result

    def test_unlock_correct_password(self, locked_rooms):
        room_a, _ = locked_rooms
        player = Player("Tester")
        player.current_room = room_a
        with patch("builtins.input", return_value="secret"):
            result = room_a.unlock(player, "north")
        assert room_a.exits["north"].locked is False
        assert "click" in result.lower()

    def test_unlock_wrong_password(self, locked_rooms):
        room_a, _ = locked_rooms
        player = Player("Tester")
        player.current_room = room_a
        with patch("builtins.input", return_value="wrong"):
            result = room_a.unlock(player, "north")
        assert room_a.exits["north"].locked is True
        assert "wrong" in result.lower()


class TestExit:
    def test_exit_creation(self):
        exit_ = Exit("north", "Library", "a doorway", locked=False)
        assert exit_.direction == "north"
        assert exit_.destination_name == "Library"
        assert exit_.locked is False
        assert exit_.destination is None

    def test_add_destination(self):
        room = Room("Library", "a quiet room")
        exit_ = Exit("north", "Library", "a doorway", locked=False)
        exit_.add_destination(room)
        assert exit_.destination is room
