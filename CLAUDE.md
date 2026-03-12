# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Game

```bash
python3 main.py
```

Requires Python 3.x and PyYAML (`pip install pyyaml`).

## Running Tests

```bash
# first time setup
python -m venv .venv
.venv/bin/pip install pytest

# run all tests
.venv/bin/python -m pytest tests/ -v

# run a single test file
.venv/bin/python -m pytest tests/test_rooms.py -v
```

## Architecture

This is a room-based text adventure with four core modules:

- **`main.py`** — Entry point. Calls `init()` (loads map, creates player) then runs `gameloop()`.
- **`src/cmds.py`** — Command parser. `input_parsing()` splits user input and dispatches to command handlers. Each command supports multiple synonym aliases.
- **`src/rooms.py`** — `Room` and `Exit` classes. Rooms hold exits (directional links to other rooms). Exits can be locked with a password. `Room.move()` handles movement; `Room.unlock()` handles password puzzles.
- **`src/player.py`** — `Player` class with `name`, `current_room`, and `inventory`.
- **`src/read_map_data.py`** — Loads `bin/map_data/escapeRoom.yaml` in two passes: first creates all Room/Exit objects, then links exits to destination Room references.

**Data flow:** `main.py` → `get_rooms()` builds the room graph from YAML → `Player` created → game loop calls `input_parsing()` → command handlers mutate `player.current_room` and `player.inventory`.

## Map Data

The game world is defined in `bin/map_data/escapeRoom.yaml`. Each room entry specifies its name, description, and exits. Each exit has a direction, destination room name, description, locked flag, and optional password. See `bin/map_data/map_format.yaml` for the schema.

## Git Workflow

Per `docs/gitrules.md`:
- `main` — release branch, no direct commits
- `dev` — integration branch, requires peer review to merge
- `task/*` — feature branches (camelCase, e.g. `task/helpPage`)
- `docs/*` — documentation branches (no merge request needed)
