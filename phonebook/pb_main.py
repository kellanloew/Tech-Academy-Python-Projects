#Python Version 3.6.6
#Author: Kellan Loew (code-along)
#Tested OS: Works with and tested on Windows 10

#Now we import tkinter gui library
from tkinter import *
import tkinter as tk
#Importing other python files/modules
import functions
import gui

#Frame is the Tkinter class that our own class will inherit from
class ParentWindow(Frame):
	def __init__(self, master, *args, **kwargs): #init initializes the class of ParentWindow.
		#Args and kwargs allow unlimited/undefined arguments passed into the parameters of the function
		Frame.__init__(self, master, *args, **kwargs) #init initializes the Frame Class from Tkinter.

		#Master Frame Config
		self.master = master #The first/chief window that opens up
		self.master.minsize(500, 300) #Width, height
		self.master.maxsize(500, 300)
		#Center the App on the screen
		functions.center_window(self,500,300) #Our own function
		self.master.title("Phonebook")
		self.master.configure(bg="#eff0f2")
		#This protocol is a tkinter method called when user goes to close the program (only for windows)
		self.master.protocol("WM_DELETE_WINDOW", lambda: functions.ask_quit(self))

		#Load in GUI from gui module
		gui.load_gui(self)

if __name__ == "__main__":
	rooter = tk.Tk() #We run the TK interpreter from Tkinter and call it "rooter"
	App = ParentWindow(rooter) #Then we call/run App which is the class ParentWindow
	# which has inherited from Tkinter
	rooter.mainloop()
