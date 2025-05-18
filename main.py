import importlib
import os
from commands import commands


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
    cmds_dir = 'cmds'
    for filename in os.listdir(cmds_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f'{cmds_dir}.{filename.replace('.py', '')}'
            module = importlib.import_module(module_name)
            cmd_data = module.get_cmd()
            commands[cmd_data['name']] = cmd_data
    return commands


main()
