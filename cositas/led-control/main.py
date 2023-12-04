# -*- coding: utf-8 -*-
"""
Created on Tue May 31 07:55:18 2022

@author: Ing. Edison Sásig

@web: www.roboticoss.com

"""

from pyModbusTCP.client import ModbusClient #pip install pyModbusTCP
from tkinter import Tk, Button
import tkinter.font as font

def onClosing():
    root.destroy()      #Cierra la ventana creada
    client.close()

def onButton():
    client.write_single_coil(LED_COIL, 1)

def offButton():
    client.write_single_coil(LED_COIL, 0)

SERVER_HOST = "192.168.43.141"
SERVER_PORT = 502
LED_COIL = 0

client = ModbusClient(host= SERVER_HOST, port=SERVER_PORT, auto_open=True, debug=False)

root = Tk() #Inicializar el root de Tkinter / Initializate the root Tkinter widget
root.protocol("WM_DELETE_WINDOW", onClosing) #Protocolo al usar al pulsar en la X de cierre/ #Protocol when pressing on the close window
root.title("WIFI LED Control") #Titulo de la ventana / Title window
root.configure(bg='#ffffff')

myFont = font.Font(size=20)


button1 = Button(root,text ="Encender",command=onButton,bg='#35B94B',fg='#ffffff',height = 2,width = 20)
button1['font'] = myFont
button1.pack(padx=20,pady=10)

button2 = Button(root,text ="Apagar",command=offButton,bg='#EC2424',fg='#ffffff', height = 2, width = 20)
button2['font'] = myFont
button2.pack(padx=20,pady=10)

root.mainloop()
