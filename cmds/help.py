def help(cmds):
    print('Help')


def get_cmd():
    return {
        'name': 'help',
        'synonyms': ['help', 'h'],
        'function': help,
        'definition': 'Show help message'
    }
