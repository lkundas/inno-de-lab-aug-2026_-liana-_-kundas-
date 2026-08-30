#Task6
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

#Task 1
name = input("Как тебя зовут? ")
print("Привет,", name, "! Приятно познакомиться")


#Task 2
length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))

square = length * width
print("Площадь прямоугольника:", square)

#Task 3
celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = celsius * 9 / 5 + 32
print(celsius, "°C это", fahrenheit, "°F")

#Task4
number = int(input("Введите целое число: "))

if number % 2 == 0:
    print(f"Число {number} — чётное.")
else:
    print(f"Число {number} — нечётное.")

#Task5
import random

secret_number = random.randint(1, 20)
attempts = 5

print("Я загадал число от 1 до 20. У тебя 5 попыток!")

while attempts > 0:
    guess = int(input("Введите число: "))

    if guess == secret_number:
        print("Ты угадала! Отличная работа.")
        break
    elif guess < secret_number:
        attempts -= 1
        print(f"Слишком мало! Осталось попыток: {attempts}")
    else:
        attempts -= 1
        print(f"Слишком много! Осталось попыток: {attempts}")

if attempts == 0 and guess != secret_number:
    print(f"Попытки закончились. Я загадал число: {secret_number}")
