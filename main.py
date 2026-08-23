num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Выберите оператор (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Неверный оператор!")