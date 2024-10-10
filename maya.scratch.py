import consts
from screen import *
import tkinter
from PIL import Image, ImageTk

def create_welcome_screen_1(screen, donor_screen, soldier_screen):
    frame = tk.Frame(width=consts.WINDOW_WIDTH, height=consts.WINDOW_HEIGHT)

    tkinter.Label(frame, text="Welcome to DonationNation!", font=consts.FONT_TUPLE, fg="green").place(relx=0.2, rely=0.1)
    tkinter.Label(frame, text="Are you a soldier or a donor?", font=consts.FONT_TUPLE, fg="green").place(relx=0.18, rely=0.3)
    tkinter.Button(frame, text="Soldier", command=lambda: show_frame(soldier_screen), font=consts.FONT_TUPLE).place(relx=0.18, rely=0.5)
    tkinter.Button(frame, text="Donor", command=lambda: show_frame(donor_screen), font=consts.FONT_TUPLE, bg="green").place(relx=0.4, rely=0.5)

    return frame

def main():
    root = tk.Tk()
    root.geometry("800x800")
    root.title("DonationNation")

    # Create screens
    wrong_screen = wrong(root)
    action_soldier_screen = create_action_soldier_screen(root)
    thank_you_screen = create_thank_you_screen(root)
    details_screen = create_details_screen(root, thank_you_screen)
    donor_screen = create_donor_screen(root, details_screen, wrong_screen)
    soldier_screen = create_soldier_screen(root, action_soldier_screen)
    welcome_screen = create_welcome_screen_1(root, donor_screen, soldier_screen)

    # Add logo
    logo = Image.open("media/logo.png")
    logo = logo.resize((100, 100), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(logo)
    tkinter.Label(root, image=photo_image).place(relx=0.7, rely=0.7)

    # Add screens to the main window
    welcome_screen.grid(row=0, column=0, sticky="nsew")
    donor_screen.grid(row=0, column=0, sticky="nsew")
    soldier_screen.grid(row=0, column=0, sticky="nsew")
    details_screen.grid(row=0, column=0, sticky="nsew")
    thank_you_screen.grid(row=0, column=0, sticky="nsew")
    action_soldier_screen.grid(row=0, column=0, sticky="nsew")
    wrong_screen.grid(row=0, column=0, sticky="nsew")
    # Show welcome screen
    show_frame(welcome_screen)

    root.mainloop()


main()
