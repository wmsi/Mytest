import serial
import tkinter
import asyncio
import websockets

#opens the serial port that will be read from
ser = serial.Serial('/dev/ttyUSB1', 115200)
ser.isOpen()
s = [0,1]
count = 0

        
while True:
        line = ser.readline()
        print (line[:-2])
        if (count == 0):
            new_char = input('press to continue ')
            ser.write(b'new_char')
        count += 1
