from tkinter import *
import tkinter as tk
import mysql.connector as sql 



root = tk.Tk()
root.geometry("600x400") #size of window

# ---hello world---------
# a = Label(root, text="Hello, World!")
# a.pack()

# Program to make a simple login screen
name_var = tk.StringVar() 
email_var = tk.StringVar() 

mydb = mysql.connector.connect(
  host="localhost",
  user="rohan",
  password="password23"
)

mycursor = mydb.cursor()


def submit():
 
    name=name_var.get()
    email=email_var.get()
     
    print("The name is : " + name)
    print("The email is : " + email)
     
    name_var.set("")
    email_var.set("")

# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
email_label = tk.Label(root, text = 'email', font = ('calibre',10,'bold'))
  
# creating a entry for password
email_entry=tk.Entry(root, textvariable = email_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
email_label.grid(row=1,column=0)
email_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)





root.mainloop()
