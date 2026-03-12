import pytest
from src.rooms import Room, Exit
from src.player import Player
import src.cmds as cmds


@pytest.fixture
def player_in_room():
    """Player in a room with one unlocked exit north and one locked exit east."""
    hall = Room("Hall", "a dusty hall")
    library = Room("Library", "a quiet library")
    armory = Room("Armory", "a weapon-filled room")

    exit_north = Exit("north", "Library", "an archway", locked=False)
    exit_north.add_destination(library)
    hall.add_exit("north", exit_north)

    exit_east = Exit("east", "Armory", "a heavy door", locked=True, password="hunt")
    exit_east.add_destination(armory)
    hall.add_exit("east", exit_east)

    player = Player("Tester")
    player.current_room = hall
    return player


class TestMove:
    def test_move_to_valid_room(self, player_in_room):
        cmds.input_parsing(player_in_room, "move north")
        assert player_in_room.current_room.name == "Library"

    def test_move_shorthand_verb(self, player_in_room):
        cmds.input_parsing(player_in_room, "go north")
        assert player_in_room.current_room.name == "Library"

    def test_move_bare_direction(self, player_in_room):
        cmds.input_parsing(player_in_room, "n")
        assert player_in_room.current_room.name == "Library"

    def test_move_no_direction_prints_prompt(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "move")
        assert "direction" in capsys.readouterr().out.lower()

    def test_move_invalid_direction_stays_in_room(self, player_in_room):
        original_room = player_in_room.current_room
        cmds.input_parsing(player_in_room, "move south")
        assert player_in_room.current_room is original_room

    def test_move_into_locked_door_stays_in_room(self, player_in_room):
        original_room = player_in_room.current_room
        cmds.input_parsing(player_in_room, "move east")
        assert player_in_room.current_room is original_room


class TestCheck:
    def test_check_empty_inventory(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "check inventory")
        assert "empty" in capsys.readouterr().out.lower()

    def test_check_inventory_with_item(self, player_in_room, capsys):
        player_in_room.add_to_inv("torch")
        cmds.input_parsing(player_in_room, "check inventory")
        assert "torch" in capsys.readouterr().out.lower()

    def test_check_inventory_shorthand(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "check i")
        assert "empty" in capsys.readouterr().out.lower()

    def test_check_no_secondary_prints_prompt(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "check")
        assert "check what" in capsys.readouterr().out.lower()


class TestGrab:
    def test_grab_adds_to_inventory(self, player_in_room):
        cmds.input_parsing(player_in_room, "grab key")
        assert "key" in player_in_room.inventory

    def test_grab_no_item_prints_prompt(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "grab")
        assert "grab what" in capsys.readouterr().out.lower()


class TestUnlock:
    def test_unlock_with_correct_password(self, player_in_room):
        from unittest.mock import patch
        with patch("builtins.input", return_value="hunt"):
            cmds.input_parsing(player_in_room, "unlock east")
        assert player_in_room.current_room.exits["east"].locked is False

    def test_unlock_no_direction_prints_prompt(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "unlock")
        assert "direction" in capsys.readouterr().out.lower()


class TestHelpAndLearn:
    def test_help_no_args_prints_something(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "help")
        assert capsys.readouterr().out.strip() != ""

    def test_help_valid_command(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "help move")
        assert "move" in capsys.readouterr().out.lower()

    def test_help_invalid_command(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "help flibbertigibbet")
        assert "not a valid command" in capsys.readouterr().out.lower()

    def test_learn_no_args_prints_instructions(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "learn")
        assert "learn" in capsys.readouterr().out.lower()

    def test_learn_valid_command(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "learn move")
        assert "move" in capsys.readouterr().out.lower()


class TestInvalidCommand:
    def test_unknown_command_prints_error(self, player_in_room, capsys):
        cmds.input_parsing(player_in_room, "flibbertigibbet")
        assert "not a valid command" in capsys.readouterr().out.lower()
