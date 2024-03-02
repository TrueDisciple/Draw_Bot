from Wcommands import Wcommands
import random

commands = []

for i in range(40):
    command = random.randint(0,1)
    if command == 0:
        command = 'LINE'
        for i in range(4):
            pos = random.randint(0, 1000)
            command += f' {pos}'
        commands.append(command)
    else:
        command = 'CIRCLE'
        for i in range(3):
            pos = random.randint(0, 1000)
            command += f' {pos}'
        commands.append(command)




if __name__ == '__main__':
    new_open_file = Wcommands(commands=commands)
    # Commands array order StartX StartY EndX EndY
    new_open_file.write_file(fileName='test.hack', writeType='w', commands=commands)


