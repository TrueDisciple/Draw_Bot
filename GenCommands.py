from Wcommands import Wcommands
import random


def randCommands():
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
        return commands
    

def genCommands():
    commands = []
    userContinue = True
    print("This is the Base Interface: if you need help with commands type help. Type done when through with instructions or Exit to leave program")
    while userContinue:
        print("Enter the command you would like to perform.\n")
        userCom = input("COMMAND (ALL CAPS) : ")
        
        
        if userCom == 'LINE':
            print("Enter the location information you would like to perform.\n")
            startX = input("Start X: ")
            startY = input("Start Y: ")
            endX = input("End X: ")
            endY = input("End Y: ")
            if not startX.isdigit() or not startY.isdigit() or not endX.isdigit() or not endY.isdigit():
                print("That is not correct please try again")
                continue
            
            commands.append(f"{userCom} {startX} {startY} {endX} {endY}")
            print("Line added successfully")

        elif userCom == 'CIRCLE':
            print("Enter the location information you would like to perform.\n")
            startX = input("Start X: ")
            startY = input("Start Y: ")
            radius = input("Radius: ")
            if not startX.isdigit() or not startY.isdigit() or not radius.isdigit():
                print("That is not correct please try again")
                break
            
            commands.append(f"{userCom} {startX} {startY} {radius}")
            print("Circle added successfully")

        elif userCom.upper() == "DONE" or userCom.upper() == "EXIT":
            userContinue = False


    print("Thank you. Goodbye.")
    return commands


def reciever(args):
    new_open_file = Wcommands(commands=args)
    new_open_file.write_file(fileName='test.hack', writeType='w', commands=args)


# if __name__ == '__main__':
#     # Back up works but is rather slow to enter. Extreamly slow!
#     #uicommands = genCommands()
#     uicommands = randCommands()
#     new_open_file = Wcommands(commands=uicommands)
#     # Commands array order StartX StartY EndX EndY
#     new_open_file.write_file(fileName='test.hack', writeType='w', commands=uicommands)


