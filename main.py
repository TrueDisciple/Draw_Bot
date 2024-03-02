from Wcommands import Wcommands

if __name__ == '__main__':
    new_open_file = Wcommands('LINE', ['command', 'commandL', 'straight'])
    new_open_file.write_file(fileName='test.hack', writeType='w', commandType='LINE', commands=['right', 'left', 'straight'])


