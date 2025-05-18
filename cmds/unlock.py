def unlock(cmds):
    print('Unlock')


def get_cmd():
    return {
        'name': 'unlock',
        'synonyms': ['unlock', 'u', 'open', 'o'],
        'function': unlock,
        'definition': 'Unlock door or object'
    }
