def move(cmds):
    print('Move')


def get_cmd():
    return {
        'name': 'move',
        'synonyms': ['move', 'm', 'go', 'g'],
        'function': move,
        'definition': 'Move to another location.'
    }
