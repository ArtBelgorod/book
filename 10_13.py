import json

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username,f)
    return username

def great_user():
    username = get_stored_username()
    otvet = input("Вы "+ username + "? ('y' or 'n') ")
    if otvet == 'y':
        print(f"Добро пожаловать обратно, {username}!")
    else:
        username = get_new_username()
        print(f"Мы запомнили Вас, {username}!")

great_user()



