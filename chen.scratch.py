import tkinter as tk
import consts
from tkinter import OptionMenu, StringVar

def create_thank_you_screen(screen):
    frame = tk.Frame(screen)

    details_text = tk.Label(frame, text="Thank you!", font= ('Ariel', 50))
    details_text.grid(row=0, column=0)

    return frame

def create_details_screen(screen, thank_you_screen):
    frame = tk.Frame(screen)

    frame.grid(row=0, column=0)

    details_text = tk.Label(frame, text="enter your details:")
    details_text.grid(row=0, column=0)

    email_entry = tk.Entry(frame, width= 20, font=('Arial', 10))
    email_entry.grid(row=1, column=1)

    email_text = tk.Label(frame, text="email:")
    email_text.grid(row=1, column=0)

    amount_entry = tk.Entry(frame, width= 20, font=('Arial', 10))
    amount_entry.grid(row=3, column=1)

    amount_text = tk.Label(frame, text="amount:")
    amount_text.grid(row=3, column=0)

    notes_entry = tk.Entry(frame, width= 40, font=('Arial', 10))
    notes_entry.grid(row=5, column=1)

    notes_text = tk.Label(frame, text="notes:")
    notes_text.grid(row=5, column=0)

    button = tk.Button(frame, text="Submit", command=lambda: show_frame(thank_you_screen))
    button.grid(row=6, column=1)

    return frame


def show_base(frame, details_screen):
    clicked = StringVar()
    clicked.set("base")

    drop = OptionMenu(frame, clicked, "Monday", "Tuesday", "Wednesday")
    drop.grid(row=3, column=1)

    button = tk.Button(frame, text="done", command=lambda: show_frame(details_screen))
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



def create_donor_screen(screen, details_screen):
    frame = tk.Frame(screen)

    clicked = StringVar()
    clicked.set("choose gear to donate")

    drop = OptionMenu(frame, clicked, "Monday", "Tuesday", "Wednesday")
    drop.grid(row=0, column=1)

    button = tk.Button(frame, text="done", command= lambda: show_base(frame, details_screen))
    button.grid(row=1, column=1)

    return frame

def create_soldier_screen(screen, action_soldier_screen):
    frame = tk.Frame(screen)

    clicked = StringVar()
    clicked.set("choose base")

    drop = OptionMenu(frame, clicked, "Monday", "Tuesday", "Wednesday")
    drop.grid(row=0, column=1)

    base_code_text = tk.Label(frame, text="base code:")
    base_code_text.grid(row=1, column=0)

    email_entry = tk.Entry(frame, width=20, font=('Arial', 10))
    email_entry.grid(row=1, column=1)

    button = tk.Button(frame, text="Submit", command=lambda: show_frame(action_soldier_screen))
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
def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("DonationNation")

    # Create screens
    action_soldier_screen = create_action_soldier_screen(root)
    thank_you_screen = create_thank_you_screen(root)
    details_screen = create_details_screen(root, thank_you_screen)
    donor_screen = create_donor_screen(root, details_screen)
    soldier_screen = create_soldier_screen(root, action_soldier_screen)
    welcome_screen = create_welcome_screen(root, donor_screen, soldier_screen)

    # Add screens to the main window
    welcome_screen.grid(row=0, column=0, sticky="nsew")
    donor_screen.grid(row=0, column=0, sticky="nsew")
    soldier_screen.grid(row=0, column=0, sticky="nsew")
    details_screen.grid(row=0, column=0, sticky="nsew")
    thank_you_screen.grid(row=0, column=0, sticky="nsew")
    action_soldier_screen.grid(row=0, column=0, sticky="nsew")

    # Show welcome screen
    show_frame(welcome_screen)

    root.mainloop()

main()
