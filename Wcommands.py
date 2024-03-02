class Wcommands:
    def __init__(self, commands):
        self.commands = commands

    def write_file(self, fileName, writeType, commands):
        with open(fileName, writeType, encoding='utf-8') as open_file:
            open_file.write('BREAK BREAK\n')
            for shape in commands:
                prevPos = None
                for pos in shape:
                    if prevPos:
                        open_file.write(f'LINE {round(prevPos[0])} {round(prevPos[1])} {round(pos[0])} {round(pos[1])} \n')
                    prevPos = pos
            open_file.write("END")
            open_file.close()

