from Tkinter import *
from config.connect import Config

arduinoConnection = None

def config():
	configWindow = Tk()
	configWindow.title("Configuration Panel")
	configWindow.minsize(400,300)
	configWindow.geometry("400x300")
	path = StringVar()
	pathValue = Entry(configWindow, textvariable=path)
	pathValue.focus_set()
	pathValue.pack(pady=20, padx=20)
	port = 9600
	portValue = Entry(configWindow)
	portValue.insert(END, port)
	portValue.pack(pady=20, padx=20)	
	b = Button(configWindow, command=lambda: configFx(configWindow, pathValue.get(), portValue.get()), text="Apply Changes")
	b.place(relx=1.0, rely=1.0, anchor=SE)

def configFx(root, device, port):
	global arduinoConnection
	arduinoConnection = Config(device, port).getConnection()
	if "Error" in arduinoConnection :
		error = Label(root, text="Error while connecting!")
		error.pack()
	else :
		print "Connection : "+arduinoConnection
		root.destroy()

master = Tk()
master.title("Blood Pressure Visualizer")
master.minsize(400,450)
master.geometry("400x450")

menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)

configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Configure", command=config)
menubar.add_cascade(label="Configuration", menu=configmenu)

Label(master, text="Blood Pressure = None").pack(pady=20, padx=50)

master.config(menu=menubar)
master.mainloop()
