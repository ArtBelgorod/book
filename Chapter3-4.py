import os

# Первая часть
numbers = ['one', 'two', 'three', 'four']
for i in range(len(numbers)):
    print(numbers[i])
print(f"Number - {numbers[0]}")
# Вторая часть
guests = ["Александр Поветкин", "Александр Пушкин", "Федор Емельяненко"]
for i in range(len(guests)):
    print(f"Приглашение на обед -  {guests[i]}.")
print(guests[-1], "не придет.")
del guests[-1]
guests.append("Хабиб Нурмагомедов")
for i in range(len(guests)):
    print(f"Приглашение на обед -  {guests[i]}.")
# Третья часть
print("Гостей будет больше!")
guests.insert(0, "Александр Шлеменко")
guests.insert(2, "Александр Карелин")
guests.append("Магомед Исмаилов")
for i in range(len(guests)):
    print(f"Приглашение на обед -  {guests[i]}.")
# Четвертая часть
print("Гостей будет двое!")
i = len(guests)
while i > 2:
    print(f"Мы сожалеем, {guests.pop()} не придет")
    i = len(guests)
for i in range(len(guests)):
    print(f"Приглашение на обед в силе -  {guests[i]}.")
del guests[1]
del guests[0]
print("Список гостей - ", guests)

# Сортировка
countries = ['Spain', 'Argentina', 'Goa', 'Bali', 'Norway']
print("Исходный - ", countries)
print(sorted(countries))
print("После сортировки - ", countries)
print(sorted(countries, reverse=True))
print("После сортировки в обратном - ", countries)
countries.reverse()
print("Изменили порядок -", countries)
countries.reverse()
print("Изменили порядок -", countries)
countries.sort()
print("Изменили порядок 1 раз sort -", countries)
countries.sort(reverse=True)
print("Изменили порядок 2 раз sort -", countries)

# Глава 4
print("---------------------------")
pizzas = ['pepperoni', 'margarita', 'Bananas']
for pizza in pizzas:
    print(f"I like {pizza} pizza.\n")
print("I really love pizza!")

print("---------------------------")
animals = ['dog', 'cat', 'elephant']
for animal in animals:
    print(f"A {animal} would make pizza.\n")
print("Any of these animals would make pizza!")
os.system('cls')
values = [i for i in range(1, 21)]
print(values)
os.system('cls')
values1 = [i for i in range(1, 1000001)]
print(min(values1), max(values1))
print(sum(values1))
values2 = [i for i in range(1, 21, 2)]
print(values2)
values3 = [i for i in range(3, 31, 3)]
print(values3)

values4 = [i ** 3 for i in range(1, 11)]
print(values4)
print(f"Первые три элемента списка -  {values4[:3]}")
print(f"Три элемента списка из середины -  {values4[4:7]}")
print(f"Последние три элемента списка -  {values4[-3:]}")

print("---------------------------")
my_pizzas = ['pepperoni', 'margarita', 'Bananas']
my_friend_pizzas = my_pizzas[:]
my_pizzas.append("chili")
my_friend_pizzas.append("ice")
print(my_pizzas)
print(my_friend_pizzas)

my_pizzas2 = ('pepperoni', 'margarita', 'Bananas')
print(my_pizzas2)
my_pizzas2 = ('pepperoni', 'margarita', 'Bananas', 'beer')
print(my_pizzas2)
for i in range(len(my_pizzas2)):
    print(my_pizzas2[i])
