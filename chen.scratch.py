import tkinter as tk
import consts
from tkinter import OptionMenu, StringVar

def create_details_screen(screen):
    frame = tk.Frame(screen)
    frame.grid(row=0, column=0)

    entry = tk.Entry(frame)
    entry.grid(row=0, column=0)


def show_base(frame):
    clicked = StringVar()
    clicked.set("base")

    drop = OptionMenu(frame, clicked, "Monday", "Tuesday", "Wednesday")
    drop.grid(row=3, column=1)

    button = tk.Button(frame, text="done", command=lambda: details)
    button.grid(row=4, column=1)

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

def create_donor_screen(screen):
    frame = tk.Frame(screen)

    clicked = StringVar()
    clicked.set("choose day")

    drop = OptionMenu(frame, clicked, "Monday", "Tuesday", "Wednesday")
    drop.grid(row=0, column=1)

    button = tk.Button(frame, text="done", command= lambda: show_base(frame))
    button.grid(row=1, column=1)

    return frame

def create_soldier_screen(screen):
    frame = tk.Frame(screen)

    welcome_text = tk.Label(frame, text="yay")
    welcome_text.grid(row=0, column=1)

    return frame

def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("DonationNation")

    # Create screens
    details_screen = create_details_screen()
    donor_screen = create_donor_screen(root)
    soldier_screen = create_soldier_screen(root)
    welcome_screen = create_welcome_screen(root, donor_screen, soldier_screen)

    # Add screens to the main window
    welcome_screen.grid(row=0, column=0, sticky="nsew")
    donor_screen.grid(row=0, column=0, sticky="nsew")
    soldier_screen.grid(row=0, column=0, sticky="nsew")

    # Show welcome screen
    show_frame(welcome_screen)

    root.mainloop()

main()
