import consts


def soldier_login():
    logged_in = False
    counter = 0
    while not logged_in and counter < consts.MAX_LOGIN_TRIES:
        base = "" # Call function to make dropdown menu
        base_code = "" # Call function to write whatever
        counter += 1
        if base in consts.BASE_CODES_DICT:
            if consts.BASE_CODES_DICT[base] == base_code:
                logged_in = True
