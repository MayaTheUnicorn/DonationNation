import tkinter as tk
import consts


def soldier_login(root):
    logged_in = False
    counter = 0
    while not logged_in and counter < consts.MAX_LOGIN_TRIES:
        bases_dropdown(root)
        base = "" # Call function to make dropdown menu
        base_code = "" # Call function to write whatever
        counter += 1
        if base in consts.BASE_CODES_DICT:
            if consts.BASE_CODES_DICT[base] == base_code:
                logged_in = True


def bases_dropdown(root):
    clicked = tk.StringVar()
    clicked.set("Choose your base")
    drop = tk.OptionMenu(root, clicked, consts.BASE_LIST)
    drop.pack()
