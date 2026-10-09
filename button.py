# import necessary libraries
from tkinter import  *

#create window
window = Tk()
window.title('Event Handler')
window.geometry('100x100')

#event handler for keypress
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
    
#bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

#event handler for button click
def handle_click(event):
    print("\n Button was clicked")
    
button = Button(text="Click me!")
button.pack()

#bind click event to handle_click()
button.bind("<Button-1>", handle_click)

#start the GUI event loop
window.mainloop()