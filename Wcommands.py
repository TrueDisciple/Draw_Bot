class Wcommands:
    def __init__(self, commandType, commands):
        self.com_type = commandType
        self.commands = commands

    def write_file(self, fileName, writeType, commandType, commands):
        with open(fileName, writeType, encoding='utf-8') as open_file:
            open_file.write('BREAK BREAK\n')
            command_line = commandType
            for com in commands:
                command_line += f" {com}"
            open_file.write(command_line + '\n')


