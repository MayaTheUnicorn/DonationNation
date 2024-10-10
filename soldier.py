import tkinter as tk
import consts


# Check if soldier entered correct password
def soldier_login(choice_base_code):
    base_choice, base_code = choice_base_code
    if consts.BASE_CODES_DICT[base_choice] == base_code:
        return True
    else:
        return False
