import tkinter as tk
from tkinter import ttk

#establishing Tk window
window = tk.Tk()
#give the window TK as name
window.title('D and D Player Run')
#establish size of window
window.geometry('400x200')

#creating widget
title_label = ttk.Label(master = window, text = 'Please Select A Race : ')
title_label.pack()


#where we run the mainloop of the function
window.mainloop()

