import json
filename = "num.json"
try:
    with open (filename) as f:
        num = json.load(f)
except FileNotFoundError:
    num = int(input("Введите Ваше любимое число - "))
    filename = "num.json"
    with open(filename, 'w') as f:
        json.dump(num, f)
        print("Мы Вас запомнили!")
else:
    print(f"Ваше любимое число -  {num}")

