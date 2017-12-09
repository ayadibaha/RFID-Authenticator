#!/usr/bin/python

import serial
import serial.tools.list_ports
from Tkinter import *
#from config.connect import *
from config.db import Db

arduinoConnection = None

'''def config():
	configWindow = Tk()
	configWindow.title("Configuration Panel")
	configWindow.minsize(400,300)
	configWindow.geometry("400x300")
	b = Button(configWindow, command=lambda: configFx(configWindow), text="Connect to device")
	b.place(relx=0.5, rely=0.5, anchor=CENTER)

def configFx(root):
	global arduinoConnection
	arduinoConnection = Config().getConnection()
	if "Error" in arduinoConnection :
		error = Label(root, text=arduinoConnection)
		error.pack()
	else :
		print "Connection : "+arduinoConnection
		root.destroy()
'''
master = Tk()
master.title("Get your informations")
master.minsize(400,450)
master.geometry("400x450")

menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)

'''configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Configure", command=config)
menubar.add_cascade(label="Configuration", menu=configmenu)
'''
# Cursor sqlite
cursor = Db().getCursor()
code = str(cursor.execute('''SELECT code FROM users''').fetchone()[0])
Label(master, text="Code de la carte "+code).pack(pady=20, padx=50)
master.config(menu=menubar)
connection = serial.Serial("/dev/ttyACM0",9600)
while True:
	print "in while"
	code = connection.readline()
	print code	
	#username = str(cursor.execute('SELECT * FROM users WHERE code='+code).fetchone()[1])
	'''if username:
		print username	
		Label(master, text="User "+username+" Authenticated").pack(pady=30, padx=50)
	'''
master.mainloop()
