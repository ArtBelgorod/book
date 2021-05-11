with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print("--------------------")
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print("--------------------")
with open('learning_p.txt') as file_object:
    contents = file_object.read()
print(contents)
print("--------------------")
with open('learning_p.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print("--------------------")
with open('learning_p.txt') as file_object:
    lines = file_object.readlines()
stroka = ""
for line in lines:
    stroka += line.strip()+"\n"
print(stroka.replace("Python","C++"))
print ("------------------")
name = input("Введите имя - ")
with open('guest.txt','w') as file_object:
    file_object.write(name)
while True:
    name = input("Введите имя - ('q' - quit) ")
    if name =='q':
        break
    print(f"Hello, {name}!")
    with open('guest_book.txt','a') as file_object:
        file_object.write(name+"\n")

while True:
    vote = input("Почему Вам нравится программировать? - ('q' - quit) ")
    if vote =='q':
        break
    with open('prog_vote.txt','a') as file_object:
        file_object.write(vote+"\n")
