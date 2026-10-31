def greet_user_v2(username="Guest"):
    print(f"V2. Good day {username}, Welcome to the application!")

def check_if_valid_username_v2(username):
    res = username.lower() in [
        "abhijit",
        "sagar",
        "manish",
        "pranjali",
    ]
    print(f"V2. Checking if {username} is valid user, result is: {res}")
