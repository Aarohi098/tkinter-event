from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Task App")
window.geometry('400x400')
window.config(bg='#ADD8E6')

routine_tasks = []
current_task_index = 0

title = Label(window, text="Routine App", font=("Arial", 16, "bold"), fg='black', bg='#ADD8E6')
title.pack(pady=10)

next_task_label = Label(window, text="Next Task: None", font=("Arial", 12), bg='#ADD8E6')
next_task_label.pack(pady=5)

user_input = Entry(window, width=30)
user_input.pack(pady=10)

def handle_click(event):
    print("Mouse clicked at position: X=" + str(event.x) + ", Y=" + str(event.y))

window.bind("<Button-1>", handle_click)

def submit_task():
    global current_task_index
    entered_text = user_input.get().strip()
    
    if not entered_text:
        messagebox.showwarning("Warning", "Please enter a task before submitting!")
        return

    print("User completed task: ", entered_text)
    
    routine_tasks.append(entered_text)
    
    current_task_index = (current_task_index + 1) % len(routine_tasks)
    next_task_label.config(text="Next Task: " + routine_tasks[current_task_index])
    
    user_input.delete(0, END)

submit_btn = Button(window, text="Submit", command=submit_task)
submit_btn.pack(pady=10)

window.mainloop()