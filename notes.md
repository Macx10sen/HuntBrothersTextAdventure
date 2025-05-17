# Command Types
* verb commands
    - move, m
        - go, g
    - look, l
        - check, c
    - unlock, u
        * key or password
        * direction or object
            * both? either or?
        - open, o
    - take, t
        - pick up
        - grab
    - drop, d
        - put down

* noun commands
    * directions
        - north, n
        - south, s
        - east, e
        - west, w
        - up, u 
        - down, d
    * objects
        * room
        * door
        * item
        * entity

* shortcut (aliases)
    - room (look room)

# Tasks
* Recognize commands and command types
    * command synonyms
* Recognize what modifyers (nouns, adjectives, adverbs) work with the command, and which don't
* Take any input and throw graceful errors
* Leave helpful messages
* Don't Repeat Yourself (how to modularize the error messages and input handling)
* Make adding new commands simple (of any type)

# Concepts
* Keep command type stored with the command and it's synonyms in a dictionary, along with the function name
    * store function in seperate python file? or create new function in current file?
    * store synonyms in a dict?
* Keep lists of each type of command and search through each list type

# psuedocode
```
commands:
    command:
        synonyms: []
        function: func()
```
```
commands:
    move:
        synonyms: ["move", "m", "go", "g"]
        function: move()
    look:
        synonyms: ["look", "l", "check", "c"]
        function: look()
    unlock:
        synonyms: ["unlock", "open", "o"]
        function: unlock()
    take:
        synonyms: ["take", "t", "pick up", "grab",]
        function: take()
    drop:
        synonyms: ["drop", "put down"]
        function: drop()
    exit:
        synonyms: ["exit"]
        function: exit()
```
```
def parse_input(cmds):
    primary_cmd, secondary_cmds* = cmds[0]
    for command in commands:
        for synonym in command.synonyms:
            if primary_cmd = synonym:
                command.function(secondary_cmds)
```
