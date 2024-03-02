class Wcommands:
    def __init__(self, commands):
        self.commands = commands

    def write_file(self, fileName, writeType, commands):
        with open(fileName, writeType, encoding='utf-8') as open_file:
            open_file.write('[')
            for shape in commands:
                prevPos = None
                open_file.write(f"LINE {round(shape[0][0])} {round(shape[0][1])},\n")
                open_file.write("PENDOWN,\n")
                for pos in shape:
                    if prevPos:
                        open_file.write(f'LINE {round(pos[0])} {round(pos[1])},\n')
                    prevPos = pos
                open_file.write("PENUP,")
            open_file.write("]")
            open_file.close()

