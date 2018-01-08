import serial
import tkinter
import asyncio
import websockets

#opens the serial port that will be read from
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.isOpen()
s = [0,1]
count = 0

attachment_sites = []

import random
import tkinter
from tkinter import ttk
from tkinter import messagebox

#class that initializes the GUI Class
class App(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.style = ttk.Style()
        self.root.title('Muscles')

        frm = ttk.Frame(self.root, borderwidth =15)
        frm.grid(rowspan = 20, columnspan = 20)
    # create the two entries and the corresponding labels
        self.label1 = ttk.Label(text = 'sensor 1')
        self.label1.grid(column = 0, row = 0, padx = 5, pady = 5)
        self.sensor1 = ttk.Entry()
        self.sensor1.grid(row=0, column =1, padx = 5)
        self.label2 = ttk.Label(text = 'sensor 2')
        self.label2.grid(column = 0, row = 1, padx = 5, pady = 5)
        self.sensor2 = ttk.Entry()
        self.sensor2.grid(row=1, column=1, padx = 5, pady = 5)
        self.sensor1.bind('<Return>', self.change_style)
    # make a Button to store the entries and quit the program
        button = ttk.Button(text='OK')
        button['command'] = self.change_style
        button.grid(row=3, column = 1, padx = 10, pady=8, sticky = 'W')

    #function that gets the values in the entry and adds to list    
    def change_style(self, event=None):
        """set the Style to the content of the Combobox"""
        content = self.sensor1.get()
        content2 = self.sensor2.get()
        try:
            attachment_sites.append(content)
            attachment_sites.append(content2)
            self.root.destroy()
        except tkinter.TclError as err:
            messagebox.showerror('Error', err)
        else:
            self.root.title(content)

app = App()
app.root.attributes('-fullscreen', False)
app.root.mainloop()

#function that prints the output to the server
@asyncio.coroutine
def muscle_output(websocket, path):
    while True:
        line = ser.readline()
        print (line[:-2])
        yield from websocket.send(line[:-2])

#Loop that handles handles assigning the two entries as the muscles
#and then starts the program
        
while True:
        line = ser.readline()
        print (line[:-2])
        if count == 0:
            ser.write(attachment_sites[count].encode('ascii'))
        if (count == 1):
            ser.write(attachment_sites[count].encode('ascii'))
        if (count == 2):
            new_char = input('press to continue ')
            ser.write(b'new_char')
        count += 1
        if count > 2:
            break

#loop that uploads the arduino output to server
start_server = websockets.serve(muscle_output, port = 3000)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()


        
    
    
