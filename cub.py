# Ex 9.13 - 9.16
# 9.13
from random import randint, choice

class Die:
    def __init__(self, cub_sides = 6):
        self.sides = cub_sides

    def roll_die(self):
        print(randint(1, self.sides))

my_die = Die()
for i in range(10):
    print(f"Бросок - {i + 1} - ", end="")
    my_die.roll_die()
print ("----------------------")
my_die = Die(10)
for i in range(10):
    print(f"Бросок - {i + 1} - ", end="")
    my_die.roll_die()
print ("----------------------")
my_die = Die(20)
for i in range(10):
    print(f"Бросок - {i + 1} - ", end="")
    my_die.roll_die()

# 9.14
my_tuple = ('1','2','3','4','5','6','7','8','9','0','g','i','r','o','d')
win_ticket = []
for i in range (4):
    win_ticket.append(choice(my_tuple))
print (f"Ваш билет - {win_ticket} выиграл!")

# 9.15
my_ticket = []
s = 0
while True:
    for i in range(4):
        my_ticket.append(choice(my_tuple))
    s+=1
    if my_ticket == win_ticket :
        break
    else:
        my_ticket = []
print (f"Попыток - {s}, my_ticket = {my_ticket}.")

# 9.16
