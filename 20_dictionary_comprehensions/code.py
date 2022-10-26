users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2,"Jose", "longp4ssword"),
    (3,"username","1234")
]

username_mapping = {user[1]: user for user in users}

username_input = str