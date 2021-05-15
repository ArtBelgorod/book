print("Введите два числа и я сложу их! \n Выход  - \" q \" ")
while True:
    num1 = input("Введите число 1 - ")
    if num1 == 'q':
        break
    num2 = input("Введите число 2 - ")
    if num2 == 'q':
        break
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Вводите числа, а не текст!")
    else:
        sum_num = num1 + num2
        print("Сумма чисел " + str(num1) + " и " + str(num2) + " равна " + str(sum_num))
