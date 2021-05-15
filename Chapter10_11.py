import json
try:
    num = int(input("Введите Ваше любимое число - "))
except ValueError:
    print("Вводите число, а не строку!")
else:
    filename = "num.json"
    with open (filename,'w') as f:
        json.dump(num,f)
        print("Мы Вас запомнили!")

