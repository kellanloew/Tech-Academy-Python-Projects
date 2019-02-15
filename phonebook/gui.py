#Python Version 3.6.6
#Author: Kellan Loew
#Phonebook project - Function Module
#Tested OS: Windows 1

from tkinter import *
import tkinter as tk

#Import our own other modules
import functions
import pb_main


def load_gui(selfie):

    #We start with tk to call Tkinter's class methods, which instantiates each object. Then we name it. Think of "selfie" as a key
    #Names for entry boxes
    selfie.label_user = tk.Label(selfie.master, text="User:")
    selfie.label_user.grid(row=0, column = 2, padx=(0,0), pady=(10,0))
    selfie.label_FName = tk.Label(selfie.master, text="First Name:")
    selfie.label_FName.grid(row=0, column=0, padx=(25,0), pady=(10,0), sticky=NW)
    selfie.label_LName = tk.Label(selfie.master, text="Last Name:")
    selfie.label_LName.grid(row=2, column=0,padx=(25,0), pady=(10,0), sticky=NW)
    selfie.label_phone = tk.Label(selfie.master, text="Phone:")
    selfie.label_phone.grid(row=4, column=0,padx=(25,0), pady=(10,0), sticky=NW)
    selfie.label_email = tk.Label(selfie.master, text="Email:")
    selfie.label_email.grid(row=6, column=0,padx=(25,0), pady=(10,0), sticky=NW)
    #Entry boxes inserted
    selfie.txt_FName = tk.Entry(selfie.master, text='')
    selfie.txt_FName.grid(row=1, column=0, columnspan=2, padx=(10, 30), sticky=N+E+W) #NEW stretches widget both E and W, at the top
    selfie.txt_LName = tk.Entry(selfie.master, text='')
    selfie.txt_LName.grid(row=3, column=0, columnspan=2, padx=(10, 20), sticky=N+E+W)
    selfie.txt_phone = tk.Entry(selfie.master, text='')
    selfie.txt_phone.grid(row=5, column=0, columnspan=2, padx=(10, 20), sticky=N+E+W)
    selfie.txt_email = tk.Entry(selfie.master, text='')
    selfie.txt_email.grid(row=7, column=0, columnspan=2, padx=(10, 20), sticky=N+E+W)
    #Listbox and scrollbar inserted
    selfie.scroll1 = Scrollbar(selfie.master, orient=VERTICAL)
    selfie.List1 = Listbox(selfie.master, exportselection=0, yscrollcommand=selfie.scroll1.set)#ES = 0 disables clipboard
    selfie.List1.bind('<<ListboxSelect>>',lambda event: functions.on_select(selfie, event)) #Bind method registers an event and calls lambda function when the listbox is clicked
    selfie.scroll1.config(command=selfie.List1.yview)
    selfie.scroll1.grid(row=1, column=5, rowspan=7, sticky=N+E+S)
    selfie.List1.grid(row=1, column=2, columnspan=3, rowspan=7, sticky=N+E+S+W)
    #Buttons inserted
    selfie.btn_add = tk.Button(selfie.master, width=12, height=2, text='Add', command=lambda: functions.addToList(selfie))
    selfie.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)
    selfie.btn_update = tk.Button(selfie.master, width=12, height=2, text='Update', command=lambda: functions.onUpdate(selfie))
    selfie.btn_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)
    selfie.btn_delete = tk.Button(selfie.master, width=12, height=2, text='Delete', command=lambda: functions.onDelete(selfie))
    selfie.btn_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W)
    selfie.btn_close = tk.Button(selfie.master, width=12, height=2, text='Close', command=lambda: functions.ask_quit(selfie))
    selfie.btn_close.grid(row=8, column=4, padx=(15,0), pady=(45,10),sticky=E)

    functions.create_db(selfie)
    functions.onRefresh(selfie)

    if __name__== "__main__":
        pass