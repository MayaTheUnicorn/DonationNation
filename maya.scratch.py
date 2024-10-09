import tkinter as tk
from tkinter import OptionMenu, StringVar
from tkinter import messagebox


def done():
    print("yay")


def OnClick_Submit():
    base_name = my_menu.get()
    messagebox.showinfo("Captured Data", base_name)


root = tk.Tk()
root.geometry("400x400")
root.title("test")

# drop down boxes
clicked = StringVar()
clicked.set("choose day")

my_menu = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday")
my_menu.pack()

button = tk.Button(root, text="done", command=done)

submit_button = tk.Button(root, text='Submit', command=OnClick_Submit)
submit_button.pack(anchor=tk.W, padx=10)


root.mainloop()

