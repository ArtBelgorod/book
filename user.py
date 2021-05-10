class User():
    def __init__(self,first_name,last_name,e_mail,location):
        self.f_name = first_name
        self.l_name = last_name
        self.mail = e_mail
        self.location = location
        self.login_attempts = 0


    def describe_user(self):
        print(f"User - {self.f_name} {self.l_name} {self.mail} {self.location}")

    def greet_user(self):
        print(f"Привет, {self.f_name.title()} {self.l_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0