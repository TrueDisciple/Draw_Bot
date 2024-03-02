# LET's Win this thing!!!!!!

#!/usr/bin/env python3
import serial
from time import sleep

command_file = ["START", "LINE 491 90 45 29", "LINE 89 45 239 91", "LINE 879 90 89 75", "LINE 45 68 90 23", "LINE 14 18 47 90"]




if __name__ == '__main__':
    ser = serial.Serial('COM4', 9600, timeout=1)
    ser.reset_input_buffer()
    

    while len(command_file) > 0:
        print(command_file)
        ser.write(command_file.pop(0).encode("utf-8") + b"\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        sleep(1)


