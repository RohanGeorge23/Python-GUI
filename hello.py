from tkinter import *
from tkinter import ttk

main_window = Tk()
#Lables - used to show output to user
Label(main_window, text="Enter your Name").grid(row=0,column=0)
Label(main_window, text="Enter your email ID").grid(row=1,column=0)
Label(main_window, text="Enter your phone number").grid(row=2,column=0)

# Text input
Name = chr(Entry(main_window, width= 50, borderwidth = 5).grid(row=0, column=1))
Email_ID = str(Entry(main_window, width= 50, borderwidth = 5).grid(row=1, column=1))
Phone = int(Entry(main_window, width= 50, borderwidth = 5).grid(row=2, column=1))

# print(Name, Email_ID, Phone)
def on_click():
    print(f"my name is :, my Email ID is:%s,and my phone number is:%s")

#Buttons
Button(main_window, text= "Submit", command=on_click).grid(row=3, column = 1)

def on_click():
    print(f"my name is {Name.get()}, my Email ID is{Email_ID.get()},and my phone number is{Phone.get()}")



main_window.mainloop()