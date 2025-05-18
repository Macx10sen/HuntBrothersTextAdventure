from commands import commands

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



def get_cmd():
    return {
        'name': 'help',
        'synonyms': ['help', 'h'],
        'function': help,
        'definition': 'Show help message'
    }
