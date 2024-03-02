# LET's Win this thing!!!!!!

#!/usr/bin/env python3
import serial
from time import sleep

command_file = ["START", "LINE 0 2000", "LINE 2000 0", "LINE 0 0"]




if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser2 = serial.Serial('', 9600, timeout=1)
    ser.reset_input_buffer()
    

    while len(command_file) > 0:
        print(command_file)
        if command_file[0] == "PENUP" or command_file[0] == "PENDOWN":
            ser2.write(command_file.pop(0).encode("utf-8") + b"\n")

        else :
            ser.write(command_file.pop(0).encode("utf-8") + b"\n")
            
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            sleep(1)


