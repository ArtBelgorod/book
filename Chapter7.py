# Ex 7.1
car = input ("Какую машину выбираете? ")
print(f"Ваша машина - {car}!")

# Ex. 7.2
quantity = int(input ("Заказываете столик на сколько человек? "))
if quantity > 8:
    print ("Придется подождать!")
else:
    print("Столик готов!")

# Ex 7.3
number = int(input("Введите число - "))
if number % 10 == 0 and number !=0:
    print("Число кратное 10")
else:
    print("Число не кратное 10")

# Ex 7.4
toppings = []
while True:
    topping = input("Input topping for pizza(if you want quit -  press 'q' ) - ")
    if topping == 'q':
        break
    else:
        toppings.append(topping)
        print (f"{topping} added in your order!")
print (toppings)

# Ex 7.5
while True:
    age = int(input("Input your age (if you want quit - press '0') - "))
    if age == 0 :
        break
    elif 0< age < 3 :
        cost = "free"
    elif 3 <= age < 12 :
        cost = "10$"
    elif age >= 12 :
        cost = "15$"
    else:
        print ("Input correct age")
        continue
    print (f"Your age is {age}, ticket cost is {cost}!")

Ex 7.6
toppings = []
active = False
while not active:
    topping = input("Input topping for pizza(if you want quit -  press 'quit' ) - ")
    if topping == 'quit':
        active = True
        continue
    else:
        toppings.append(topping)
        print (f"{topping} added in your order!")
print (toppings)

# Ex 7.7
while True:
    print("1")

Ex 7.8
sandwich_orders = ['super_san1', 'super_san2', 'super_san3']
print(sandwich_orders)
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f"I made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches :
    print (f"Finished sandwiches: {sandwich}!")
print(sandwich_orders)
finished_sandwiches.reverse()
print(finished_sandwiches)

Ex 7.9
sandwich_orders = ['pastrami','super_san1', 'pastrami','super_san2', 'pastrami','super_san3','pastrami']
print(sandwich_orders)
finished_sandwiches = []
print ("We have no pastrami!")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich != 'pastrami':
        finished_sandwiches.append(current_sandwich)

print(sandwich_orders)
finished_sandwiches.reverse()
print(finished_sandwiches)

# Ex 7.10
otpusk_dict = {}
active = True
while active:
    name = input("Input your name - ")
    otpusk = input("Where you want to rest - ")
    otpusk_dict[name] = otpusk
    repeat = input("Another man? ('y/n') ")
    while True:
        if repeat == "n":
            active = False
            break
        elif repeat == "y" :
            break
        else:
            repeat = input("Another man? ('y/n') ")
print ("\n Poll Requests\n_______________")
for name, otpusk in otpusk_dict.items():
    print(f"{name.title()} want to rest in {otpusk.title()}!")


