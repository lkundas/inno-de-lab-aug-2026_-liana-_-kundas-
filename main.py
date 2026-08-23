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