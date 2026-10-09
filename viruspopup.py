#import necessary libraries
from tkinter import  *
from tkinter import messagebox

#setup tkinter window
root = Tk()
root.geometry('200x200')

#function for displaying warning message
#this will be called once the button is clicked
#messagebox.showwarning("Window name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found")
    
#adding button widget to window
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

#start main GUI event loop
root.mainloop() 