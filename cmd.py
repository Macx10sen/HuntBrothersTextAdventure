import sys


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


commands = {}
}
