import tkinter as tk
import consts
from tkinter import OptionMenu, StringVar

import donor
import soldier


def create_thank_you_screen(screen):
    frame = tk.Frame(screen)

    details_text = tk.Label(frame, text="Thank you!", font=('Ariel', 50))
    details_text.grid(row=0, column=0)

    return frame


def create_details_screen(screen, thank_you_screen):
    frame = tk.Frame(screen)

    frame.grid(row=0, column=0)

    details_text = tk.Label(frame, text="enter your details:")
    details_text.grid(row=0, column=0)

    email_entry = tk.Entry(frame, width=20, font=('Arial', 10))
    email_entry.grid(row=1, column=1)

    email_text = tk.Label(frame, text="email:")
    email_text.grid(row=1, column=0)

    amount_entry = tk.Entry(frame, width=20, font=('Arial', 10))
    amount_entry.grid(row=3, column=1)

    amount_text = tk.Label(frame, text="amount:")
    amount_text.grid(row=3, column=0)

    notes_entry = tk.Entry(frame, width=40, font=('Arial', 10))
    notes_entry.grid(row=5, column=1)

    notes_text = tk.Label(frame, text="notes:")
    notes_text.grid(row=5, column=0)

    button = tk.Button(frame, text="Submit", command=lambda: show_frame(thank_you_screen))
    button.grid(row=6, column=1)

    return frame


def show_base(frame, details_screen, list, wrong_screen):
    if list:

        clicked = StringVar()
        clicked.set("base")

        drop = OptionMenu(frame, clicked,*list)
        drop.grid(row=3, column=1)

        button = tk.Button(frame, text="done", command=lambda: show_frame(details_screen))
        button.grid(row=4, column=1)

    else:
        show_frame(wrong_screen)

def wrong(screen):
    frame = tk.Frame(screen)

    details_text = tk.Label(frame, text="no need for this gear in any base", font=('Ariel', 15))
    details_text.grid(row=0, column=0)

    return frame



def show_frame(frame):
    frame.tkraise()


def create_welcome_screen(screen, donor_screen, soldier_screen):
    frame = tk.Frame(screen)

    welcome_text = tk.Label(frame, text="Welcome to DonationNation!")
    welcome_text.grid(row=0, column=1)

    choose_text = tk.Label(frame, text="Are you a soldier or a donor?")
    choose_text.grid(row=1, column=1)

    soldier_button = tk.Button(frame, text="Soldier", command=lambda: show_frame(soldier_screen))
    soldier_button.grid(row=3, column=1)

    donor_button = tk.Button(frame, text="Donor", command=lambda: show_frame(donor_screen))
    donor_button.grid(row=3, column=2)

    return frame

def save_for_donor(button_name):
    return donor.donation(button_name.get())

def save_for_soldier(base, code):
    checking_list = []
    checking_list.append(base.get())
    checking_list.append(code.get())
    return soldier.soldier_login(checking_list)

def test(base, code):
    if soldier.soldier_login(save_for_soldier(base, code)) == False:
        pass
    else:
        print("yes")


def create_donor_screen(screen, details_screen, wrong_screen):
    frame = tk.Frame(screen)

    clicked = StringVar()
    clicked.set("choose gear to donate")

    drop = OptionMenu(frame, clicked, *consts.GEAR_LIST)
    drop.grid(row=0, column=1)

    button = tk.Button(frame, text="done", command=lambda: [save_for_donor(clicked), show_base(frame, details_screen, save_for_donor(clicked), wrong_screen)])
    button.grid(row=1, column=1)


    return frame


def create_soldier_screen(screen, action_soldier_screen):
    frame = tk.Frame(screen)

    clicked = StringVar()
    clicked.set("choose base")

    drop = OptionMenu(frame, clicked, *consts.BASE_LIST)
    drop.grid(row=0, column=1)

    base_code_text = tk.Label(frame, text="base code:")
    base_code_text.grid(row=1, column=0)

    code_entry = tk.Entry(frame, width=20, font=('Arial', 10))
    code_entry.grid(row=1, column=1)

    # button = tk.Button(frame, text="Submit", command=lambda: show_frame(action_soldier_screen))
    button = tk.Button(frame, text="Submit", command=lambda: test(clicked, code_entry))
    button.grid(row=6, column=1)

    return frame


def create_action_soldier_screen(screen):
    frame = tk.Frame(screen)

    clicked = StringVar()
    clicked.set("choose action")

    drop = OptionMenu(frame, clicked, "Monday", "Tuesday", "Wednesday")
    drop.grid(row=0, column=1)

    button = tk.Button(frame, text="done", command=lambda: show_base(frame))
    button.grid(row=1, column=1)

    return frame
