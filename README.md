# Hunt Brothers Text Adventure

A collaborative text adventure game built in Python among friends — originally a way to learn Python together, grown into a side project.

## Team

| Name | Role |
|---|---|
| Kolter | Project Manager |
| Matt | Board Director |
| Marcus | Lead Engineer |
| Beth | KISS Tester *(later)* |
| Kambree | KISS Tester *(later)* |

## Requirements

- Python 3.x
- PyYAML — `pip install pyyaml`

## Running the Game

```bash
python3 main.py
```

You'll be prompted for your name, then dropped into the starting room. Type commands to explore.

## Commands

| Command | What it does |
|---|---|
| `move <direction>` | Move to an adjacent room (also: `go`, `walk`, `run`, `g`, `m`) |
| `<direction>` | Shorthand — just type the direction directly (e.g. `north`, `n`) |
| `check inventory` | Show your inventory (also: `check i`) |
| `check room` | Redisplay the current room (also: `check r`, `check location`) |
| `grab <item>` | Pick up an item (also: `take`, `pick`, `obtain`) |
| `unlock <direction>` | Unlock a door — you'll be prompted for a password (also: `open`) |
| `help` | List all commands |
| `help <command>` | Show accepted synonyms for a command |
| `learn <command>` | Explain what a command does |
| `exit` | Quit the game |

Directions: `north`/`n`, `south`/`s`, `east`/`e`, `west`/`w`, `northeast`/`ne`, `northwest`/`nw`, `southeast`/`se`, `southwest`/`sw`, `up`/`u`, `down`/`d`

## Current Map — Escape Room

```
         [Library]
             |
             N
             |
[Armory] -- E/W -- [Entrance Hall]  ← start
```

- **Entrance Hall** — starting room. North leads to the Library (unlocked). East leads to the Armory (locked).
- **Library** — dusty shelves and ancient tomes. Exit south back to the Entrance Hall.
- **Armory** — racks of rusty weapons. Exit west back to the Entrance Hall.

## Adding a New Map

Maps are defined in YAML under `bin/map_data/`. See `bin/map_data/map_format.yaml` for the schema. Each room lists its description and exits; each exit specifies a destination, description, and whether it's locked (with an optional password).

## Running Tests

```bash
# first time setup
python -m venv .venv
.venv/bin/pip install pytest

# run all tests
.venv/bin/python -m pytest tests/ -v
```

## Git Workflow

| Branch | Purpose |
|---|---|
| `main` | Release — no direct commits |
| `dev` | Integration — requires peer review to merge |
| `task/<name>` | Feature work (camelCase, e.g. `task/helpPage`) |
| `docs/<name>` | Documentation — no merge request needed |
