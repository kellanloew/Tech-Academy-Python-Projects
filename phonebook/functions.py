#Python Version 3.6.6
#Author: Kellan Loew
#Phonebook project - Function Module
#Tested OS: Windows 10

import os
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import sqlite3

#Import our own modules
import pb_main
import gui

def center_window(self, w, h):
    #Get user's screen size
    sWidth = self.master.winfo_screenwidth()
    sHeight = self.master.winfo_screenheight()
    #Find x,y coordinates to center app
    x = int((sWidth/2) - (w/2))
    y = int((sHeight/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if tk.messagebox.askokcancel("Exit Program", "You sure you to cancel program?"):
        self.master.destroy() #Tkinter method to close window
        os._exit(0) #Frees up memory to prevent memory leaks

def create_db(self):
    conn = sqlite3.connect("db_phonebook.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        #Commit to save changes and close DB connection
        conn.commit()
    conn.close()
    first_run(self)# Populates tables first time db is made

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '123-456-7890', 'johndoe@emailers.com')
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook(col_fname, col_lname, col_fullname, col_phone, col_email) VALUES(?,?,?,?,?)""", data)
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT (*) from tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

def on_select(self,event):
    varList = event.widget #Catches the widget that had an event
    select = varList.curselection()[0] #Gets index of selected list item
    value = varList.get(select) #Gets value from selected list item
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varbody = cur.fetchall() #The tuple returned from the database query
        for data in varbody:
            self.txt_FName.delete(0, END)
            self.txt_FName.insert(0, data[0])
            self.txt_LName.delete(0, END)
            self.txt_LName.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])

def addToList(self):
    fName = self.txt_FName.get()
    lName = self.txt_LName.get()
    #make data consistently formatted for database
    fName = fName.strip() #Remove blanks before and after user's entry
    lName = lName.strip()
    fName = fName.title() #Capitalize first letter
    lName = lName.title()
    fullName = ("{} {}".format(fName, lName)) #Create fullname
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    if(len(fName) > 0) and (len(lName) > 0) and (len(phone) > 0) and (len(email) > 0):
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT (col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(fullName))
            count = cursor.fetchone()[0]
            if count == 0: #If 0, fullname does not exist
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES(?, ?, ?, ?, ?)""", (fName, lName, fullName, phone, email))
                self.List1.insert(END, fullName) #Updates list with added item
                onClear(self) #Clears textboxes
            else: #if fullname already exists
                tk.messagebox.showerror("Name error", """{} already exists in the phonebook! Please choose a different name.""".format(fullName))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        tk.messagebox.showerror("Missing Text", "Please ensure all four fields have data.")

def onDelete(self):
    select = self.List1.get(self.List1.curselection()) #Gets index of selected list item and then value at that index
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        #Now we check count to make sure there's more than 1 record
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = tk.messagebox.askokcancel("All records associated with {} will be deleted. \nOK to proceed?".format(select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM tbl_phonebook WHERE col_fullname = '{}'".format(select))
                onDeleted(self) #Clears appropriate boxes/text
                conn.commit()
        else:
            tk.messagebox.showerror("Delete Error", """{} is the last record and cannot be deleted.""".format(select))
    conn.close()

def onDeleted(self):
    #Deletes content from textboxes
    self.txt_FName.delete(0, END)
    self.txt_LName.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    #Delete entry from listbox
    try:
        index = self.List1.curselection()[0]
        self.List1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # Deletes content from textboxes
    self.txt_FName.delete(0, END)
    self.txt_LName.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)

def onRefresh(self):
    self.List1.delete(0, END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count: #WHY THIS LOOP?
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.List1.insert(0, str(item))
                i = i + 1
    conn.close()

def onUpdate(self):
    try:
        select = self.List1.curselection()[0] #Index number
        value = self.List1.get(select) #Text value
    except:
        tk.messagebox.showinfo("Missing Selection", "No name was selected from the list. Please select a name.")
        return
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    if (len(phone) > 0) or (len(email) > 0): #ensures that data is present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            curr = conn.cursor()
            if (phone != "") or (email != ""):
                if (phone != "") and (email == ""): #If only phone has changed
                    responser = tk.messagebox.askokcancel("Update Request", """{} will be changed for {}.""".format(phone, value))
                    if responser:
                        with conn:
                            cur = conn.cursor()
                            cur.execute("""UPDATE tbl_phonebook SET col_phone = '{}' WHERE col_fullname = '{}'""".format(phone, value))
                    else:
                        tk.messagebox.showinfo("No changes have been made. You may close the window.")
                elif (phone == "") and (email != ""): #If only email has changed
                    responser = tk.messagebox.askokcancel("Update Request", """{} will be changed for {}.""".format(email, value))
                    if responser:
                        with conn:
                            cur = conn.cursor()
                            cur.execute("""UPDATE tbl_phonebook SET col_email = '{}' WHERE col_fullname = '{}'""".format(email, value))
                    else:
                        tk.messagebox.showinfo("No changes have been made. You may close the window.")
                elif (phone != "") and (email != ""):  #If email and phone have changed
                    responser = tk.messagebox.askokcancel("Update Request", """{} and {} will be changed for {}.""".format(phone, email, value))
                    if responser:
                        with conn:
                            cur = conn.cursor()
                            cur.execute("""UPDATE tbl_phonebook SET col_phone = '{}', col_email = '{}' WHERE col_fullname = '{}'""".format(phone, email, value))
                    else:
                        tk.messagebox.showinfo("No changes have been made. You may close the window.")
                onClear(self)
                conn.commit()
            else:
                tk.messagebox.showinfo("""Nothing changed. {} and {} already exist for {}.""".format(phone, email, value))
        conn.close()
    else:
        tk.messagebox.showerror("No changes have been detected. \nPlease select an entry and try again.")
    onClear(self)
if __name__ == "__main__":
    pass