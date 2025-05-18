import sys


def exit_game(cmds):
    print('\nAre you sure?')
    confirmation = input('--> ').lower()
    if confirmation in ['yes', 'y']:
        print('\nThanks for playing!')
        sys.exit(0)


def get_cmd():
    return {
        'name': 'exit',
        'synonyms': ['exit', 'quit', 'q'],
        'function': exit_game,
        'definition': 'Exit the game'
    }
