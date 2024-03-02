class Wcommands:
    def __init__(self, commands):
        self.commands = commands

    def write_file(self, fileName, writeType, commands):
        with open(fileName, writeType, encoding='utf-8') as open_file:
            open_file.write('BREAK BREAK\n')
            for com in commands:
                open_file.write(com + '\n')
                

