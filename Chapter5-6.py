import os

car = "bmw"
print("Is car == 'bmw'? I predict True.")
print(car == 'bmw')

print("\nIs car == 'ferrari'? I predict False.")
print(car == 'ferrari')

cat = "Maison"
print("\nIs cat == 'Tyson'? I predict False.")
print(cat == 'Tyson')

print("\nIs cat == 'Maison'? I predict True.")
print(cat == 'Maison')

print("\nIs cat == 'maison' and car == 'bmw'? I predict True.")
print(cat.lower() == 'maison' and car == 'bmw')

print("\nIs cat == 'maison' or car == 'Bmw'? I predict True.")
print(cat.lower() == 'maison' or car == 'Bmw')

print("\nIs cat == 'Maison' or car == 'Bmw'? I predict False.")
print(cat.lower() == 'Maison' or car == 'Bmw')

# Часть 2
allien_color = "red"
if allien_color == "green":
    print("You have 5 points!")
elif allien_color == "yellow":
    print("You have 10 points!")
else:
    print("You have 15 points!")

print("---------------------")
age = 3
if age < 2:
    print("младенец")
elif 4 > age >= 2:
    print("малыш")
elif 13 > age >= 4:
    print("ребенок")
elif 20 > age >= 13:
    print("подросток")
elif 65 > age >= 20:
    print("взрослый")
else:
    print("пожилой человек")

print("-----------------------------")
favourite_fruits = ["banana", 'apple', 'kiwi']
fruit = "pineapple"
if fruit in favourite_fruits:
    print(f"You really like {fruit}'s!")

# Chapter 3
users = ['Art', 'admin', 'Tim', 'Tanya', "Messi"]
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello, {user}, would you like a status report?")
        else:
            print(f"Hello, {user}, thank yoг for logging again?")
else:
    print("We need to ind some users")
print("----------------------------")
# 2
current_users = ['Art', 'admin', 'Tim', 'Tanya', "Messi"]
new_users = ['ARt', 'Admin', 'Timothy', 'Tanyak', "Messi_Leo"]
name_exists = False
for newuser in new_users:
    for user in current_users:
        if newuser.lower() == user.lower():
            print(f"User {newuser} also exists. Change name!")
            name_exists = True
    if not name_exists:
        print(f"Name {newuser} is free!")
    name_exists = False
# 3
print("----------------------")
numbers = [i for i in range(1, 10)]
print(numbers)

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
os.system('cls')
# Chapter 6
# Словари часть 1
man = {
    'first_name': 'Artem',
    'last_name': 'Khaimov',
    'age': 42,
    'city': 'Belgorod',
}
print(man['first_name'])
print(man['last_name'])
print(man['age'])
print(man['city'])
print("---------------")
numbers_fav = {
    'Art': 5,
    'Bob': 7,
    "Rob": 15,
    "Dan": 26,
    "Fedor": 92,
}
for f_name, f_num in numbers_fav.items():
    print(f"{f_name}'s favourite num is {f_num}!")

print("---------------")
dict_slova = {
    'tupes': "Кортежи",
    'dicts': "Словари",
    "lists": "Списки",
    "sets": "Множества",
    "for": "Циклы",
}
for f_opred, f_slovo in dict_slova.items():
    print(f"{f_opred} - это   {f_slovo}!\n")

# Словари часть 2

print("---------------")
dict_rivers = {
    'Нил': "Египет",
    'Волга': "Россия",
    "Амазонка": "Южная Америка",
    "Ганг": "Индия",
    "Хуанхэ": "Китай",
}
print("Реки:")
for f_opred in dict_rivers:
    print(f"{f_opred}!\n")
print("Страны:\n")
for f_opred in sorted(dict_rivers.values(), reverse=True):
    print(f"{f_opred}!", end=" ")

print("-------------------------")
favourite_languages = {
    'jen': "C",
    "ben": "Python",
    "den": "Ruby",
    "tim": "Pascal"
}
peoples = ['tim', 'den', 'art', 'rob']
Flag = False
for human in peoples:
    for name in favourite_languages:
        if human.lower() == name.lower():
            print(f"{human.title()}, thank you for time!")
            Flag = True
    if not Flag:
        print(f"{human.title()}, tell poll, please!")
    Flag = False

os.system('cls')
# Chapter last
man1 = {
    'first_name': 'Artem',
    'last_name': 'Khaimov',
    'age': 42,
    'city': 'Belgorod',
}
man2 = {
    'first_name': 'Andrew',
    'last_name': 'Baranov',
    'age': 35,
    'city': 'Belgorod',
}
man3 = {
    'first_name': 'Dima',
    'last_name': 'Tarasov',
    'age': 23,
    'city': 'Moscow',
}
people = [man1, man2, man3]
for chel in people:
    for key, value in chel.items():
        print(f"{key} - {value}, ", end="")
    print("\n")

# Ex 6.8
Vaska = {
    'animal': "cat",
    'owner': "Art",
}
Muska = {
    'animal': "rat",
    'owner': "Bob",
}
Puska = {
    'animal': "dog",
    'owner': "Dan",
}
pets = [Vaska, Muska, Puska]
for pet in pets:
    for key, value in pet.items():
        print(f"{key} - {value}, ", end="")
    print("\n")

# Ex. 6.9
favourite_places = {
    'Square': ["Bob", "Ben", "Dan"],
    'Big Ben': ["Art", "Bob"],
    'Luvr': ["Tanya", "Tima", "Dan"],
}
for place, names in favourite_places.items():
    print(f"{place} favourite for:")
    for name in names:
        print(f"\n{name}")
    print("\n")

# Ex. 6.10
numbers_fav = {
    'Art': [5, 7, 10],
    'Bob': [7, 15, 888],
    "Rob": [15, 36, 89],
    "Dan": [26, 74, 98],
    "Fedor": [92, 129]
}
for key,values in numbers_fav.items():
    print (f"Favourite's num for {key}:")
    for value in values:
        print(f"\n{value}")
    print("---------------")
