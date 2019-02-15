#Python Version 3.6.6

#Author: Kellan Loew

#Tested OS: Windows 10

import os
import sqlite3
import shutil
from tkinter import *
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

class ParentWin(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Master Frame Config
        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(800, 300)
        self.master.title("File Explorer")
        self.master.configure(bg="#ede8d3")
        center_window(self, 500, 300)

        self.master.grid_columnconfigure(1, weight=1, uniform="thing")
        load_gui(self)

def load_gui(self):
    #Text fields
    self.addressBar = tk.Entry(self.master, text='')
    bar1 = self.addressBar
    self.addressBar.grid(row=0, column=1, columnspan=3, padx=(15, 30), pady=(15, 0), sticky=EW)

    self.addressBar = tk.Entry(self.master, text='')
    bar2 = self.addressBar
    self.addressBar.grid(row=1, column=1, columnspan=3, padx=(15, 30), pady=(15, 0), sticky=EW)
    #Buttons
    self.btn_1 = tk.Button(self.master, height=3, width=13, wraplength=80, text='Select Source Directory...', command=lambda: openDirectory(self, bar1))
    self.btn_1.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))

    self.btn_2 = tk.Button(self.master, height=3, width=13, wraplength=80, text='Select Destination Directory...', command=lambda: openDirectory(self, bar2))
    self.btn_2.grid(row=1, column=0, padx=(15, 0), pady=(15, 0))

    self.btn_3 = tk.Button(self.master, height=3, width=13, wraplength=80, text='Move Files!', command=lambda: move_files(self, bar1, bar2))
    self.btn_3.grid(row=2, column=0, columnspan=2, padx=(15, 0), pady=(15, 15), sticky=N)

    create_db(self)

def openDirectory(self, bar):
    if bar.get() != "":
        bar.delete(0, END)
    address = tk.filedialog.askdirectory()
    bar.insert(0, address)

def move_files(self, bar1, bar2):
    count = 0
    source = bar1.get()
    dest = bar2.get()
    if (source == '') or (dest == ''):
        tk.messagebox.showerror("Folder Error", "Please select a path for both folders.")
    elif source == dest:
        tk.messagebox.showerror("Folder Error", "Source and destination cannot be the same.")
    else:
        
        list_files = os.listdir(source)

        for i in list_files:
            pair = []
            currFile = i #Saves name of current file into variable
            textFile = currFile.endswith(".txt") #gives index of found text "txt"

            if textFile == True: #If textFile = true, that means .txt has been found at end of the file name
                pair.append(currFile) #First member in list is name of file
                filepath = os.path.join(source + "\\" + currFile)
                pair.append(os.path.getmtime(filepath)) #Second member of list is timestamp
                shutil.move(filepath, dest)
                fileName = pair[0]
                time =  pair[1]
                print(pair)
                addToDB(fileName, time)
                bar1.delete(0, END)
                bar2.delete(0, END)
                count += 1
        if count == 0:
            tk.messagebox.showinfo("File Info", "There were no text files to move in the source directory.")
                

def create_db(self):
    conn = sqlite3.connect("db_textfiles.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fileName TEXT, \
                    col_time REAL \
                    );")
        conn.commit()
    conn.close()

def addToDB(fileName, time):
    conn = sqlite3.connect("db_textfiles.db")
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files (col_fileName, col_time) VALUES(?,?)", (fileName, time))
        conn.commit()
    conn.close()

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo



if __name__ == "__main__":
    root = tk.Tk() #We run the TK interpreter from Tkinter and call it "root"
    App = ParentWin(root) #Then we call/run App which is the class ParentWindow
    root.mainloop()
