# Список транзакций, полученных от платежного шлюза
raw_transactions = [
    "SUCCESS:100",
    "FAILED:50",
    "SUCCESS:-10",
    "SUCCESS:0",
    "SUCCESS:250",
    "ERROR:200",
]

# Реализация фильтрации в одну строку с помощью List Comprehension
cleaned_transactions = [
    # 4. Преобразует корректные суммы в целочисленный тип данных (int)
    # 2. Извлекает числовое значение суммы платежа
    int(tx.split(":")[1])
    for tx in raw_transactions
    # 1. Отсеивает все транзакции, не имеющие статус SUCCESS
    if tx.startswith("SUCCESS")
    # 3. Исключает аномальные транзакции с неположительной суммой (меньше или равной нулю)
    and int(tx.split(":")[1]) > 0
]

# Выводим результат
print("Очищенные транзакции:", cleaned_transactions)