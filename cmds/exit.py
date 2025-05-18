def exit_game(cmds):
    print('Exit')


def get_cmd():
    return {
        'name': 'exit',
        'synonyms': ['exit'],
        'function': exit_game,
        'definition': 'Exit the game'
    }
