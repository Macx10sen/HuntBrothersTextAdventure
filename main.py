from cmd import commands


def main():
    load_commands()
    gameloop()


def gameloop():
    print("Text Adventure Input Parsing Test")
    while True:
        cmds = input("--> ")
        parse_input(cmds)


def parse_input(cmds):
    cmds = cmds.lower().strip().split()
    if not cmds:
        print('No command entered\n')
        return
    primary_cmd, *secondary_cmds = cmds
    for command in commands:
        for synonym in commands[command]['synonyms']:
            if primary_cmd == synonym:
                commands[command]['function'](secondary_cmds)
                print()
                return
    print(f'Command Unknown: {primary_cmd}\n')


def load_commands():



main()
