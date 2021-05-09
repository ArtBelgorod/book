# Ex 9.1
class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Ресторан - {self.restaurant_name}, тип - {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, inc_num_served):
        self.number_served += inc_num_served


restaurant = Restaurant("Прага","Ресторан русской кухни")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.number_served = 4
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(6)
print(restaurant.number_served)

# Ex 9.2
restaurant1 = Restaurant("Садко","Украинская кухня")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Сулико","Ресторан грузинской кухни")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("KFC","Ресторан быстрого питания")
restaurant3.describe_restaurant()

print ("-----------------------")

# Ex 9.3
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


user1 = User("artem","khaimov","khaimov@ya.ru","belgorod")
user2 = User("nick","mukhin","nick@mail.ru","moscow")
user3 = User("ivan","rich","ivan312@nov.ru","grozny")

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()