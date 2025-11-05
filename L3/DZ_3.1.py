num_1 = int(input("Привіт, я найпростіший калькулятор! Будь ласка, введи перше число:"))
num_2 = int(input("Тепер введи друге число:"))
diya = input("Введіть дію (+, -, *, /):")
if diya == "+":
    result = num_1 + num_2
    print(f"Додавання цих чисел дає результат {result}")
elif diya == "-":
    result = num_1 - num_2
    print(f"Віднімання цих чисел дає результат {result}")
elif diya == "*":
    result = num_1 * num_2
    print(f"Множення цих чисел дає результат {result}")
elif diya == "/":
    if num_2 == 0:
        print("Перепрошую, але ділити нуль або на нуль не можна. Введіть будь-яке інше число!")
    else:
        result = num_1 / num_2
        print(f"Ділення цих чисел дає результат {result}")