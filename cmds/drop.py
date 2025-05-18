def drop(cmds):
    print('Drop')


def get_cmd():
    return {
        'name': 'drop',
        'synonyms': ['drop', 'put', 'p'],
        'function': drop,
        'definition': 'Drop item from inventory'
    }
