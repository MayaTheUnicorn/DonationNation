import openpyxl as op


# wb = op.load_workbook(r'gear_amounts.xlsx')
# ws = wb['Uvda']
# print(ws['B2'].value)
# ws['B2'].value = 5
# wb.save(r'C:\Users\kotbe\OneDrive\Desktop\Donation_Nation.xlsx')
# # print(ws.cell(row=2, column=3).value)
import tkinter as tk
from tkinter import OptionMenu, StringVar


def done():
   print("yay")


soldier_screen_action = tk.Tk()
soldier_screen_action.geometry("400x400")


clicked = StringVar()
clicked.set("choose an action")


drop = OptionMenu(soldier_screen_action, clicked, "Add gear", "Remove equipment", "Wednesday")
drop.pack()


button = tk.Button(root, text="done", command=done)


root.mainloop()






def soldier_action(logged_in):
    if logged_in:
