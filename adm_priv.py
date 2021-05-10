from user import User

class Privileges():
    def __init__(self, privileges=['разрешено добавлять сообщения', 'разрешено удалять пользователей',
                                   'разрешено банить пользователей', ]):
        self.privileges = privileges

    def show_privileges(self):
        for priv in self.privileges:
            print(f" - {priv}")

class Admin(User):
    def __init__(self, first_name, last_name, e_mail, location):
        super().__init__(first_name, last_name, e_mail, location)
        self.privileges = Privileges()