# LET's Win this thing!!!!!!

#!/usr/bin/env python3
import serial
from time import sleep

# command_file = open("filepath", "r").readlines




if __name__ == '__main__':
    ser = serial.Serial('COM4', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        ser.write(b"LINE 24 35 46 57")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        sleep(1)
