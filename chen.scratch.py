import tkinter as tk
from tkinter import Frame

def show_welcome_screen(screen):
    welcome_text = tk.Label(screen, text="Welcome to DonationNation!")
    welcome_text.grid(row=0, column=1)

    choose_text = tk.Label(screen, text="Are you a soldier or a donor?")
    choose_text.grid(row=1, column=1)

    soldier_button = tk.Button(screen, text="Soldier", command=clicked_soldier_button)
    soldier_button.grid(row=3, column=1)

    donor_button = tk.Button(screen, text="Donor", command=clicked_donor_button)
    donor_button.grid(row=3, column=2)

    screen.mainloop()


def show_donor_screen(screen):
    welcome_text = tk.Label(screen, text="Welcome to DonationNation!")
    welcome_text.grid(row=0, column=1)

def clicked_soldier_button():
    global donor_screen
    show_donor_screen(donor_screen)

def clicked_donor_button():
    #goto next screen
    pass

def main():
    root = tk.Tk()

    welcome_screen = Frame(root)
    donor_screen = Frame(root)
    soldier_screen = Frame(root)

    welcome_screen.grid(row=0, column=0)
    donor_screen.grid(row=0, column=0)
    soldier_screen.grid(row=0, column=0)


    root.geometry("400x400")
    root.title("DonationNation")

    show_welcome_screen(welcome_screen)


main()