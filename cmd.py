import sys


def move(cmds):
    print('Move')


def look(cmds):
    print("Look")


def unlock(cmds):
    print('Unlock')


def take(cmds):
    print('Take')


def drop(cmds):
    print('Drop')


def exit_game(cmds):
    print('\nAre you sure?')
    confirmation = input('--> ').lower()
    if confirmation in ['yes', 'y']:
        print('\nThanks for playing!')
        sys.exit(0)


def help(cmds):
    print('Commands:')
    print('---------')
    for command in commands:
        print(f'{command.capitalize()}: {commands[command]['definition']}')
        print('    Accepted inputs: ', end='')
        first = True
        for syn in commands[command]['synonyms']:
            if first:
                first = False
            else:
                print(', ', end='')
            print(f'{syn}', end='')
        print('\n')


commands = {
    'move': {
        'synonyms': ['move', 'm', 'go', 'g'],
        'function': move,
        'definition': 'Move to another location.'
    },
    'look': {
        'synonyms': ['look', 'l', 'check', 'c'],
        'function': look,
        'definition': 'Look around or look at specific item'
    },
    'unlock': {
        'synonyms': ['unlock', 'open', 'o'],
        'function': unlock,
        'definition': 'Unlock door or object.'
    },
    'drop': {
        'synonyms': ['drop', 'put down'],
        'function': drop,
        'definition': 'Drop item from inventory'
    },
    'exit': {
        'synonyms': ['exit'],
        'function': exit_game,
        'definition': 'Exit the game'
    },
    'help': {
        'synonyms': ['help', 'h'],
        'function': help,
        'definition': 'Show help message'
    }
}
