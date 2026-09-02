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
    # 1. Преобразует корректные суммы в целочисленный тип данных (int)
    # 2. Извлекает числовое значение суммы платежа
    int(tx.split(":")[1]) for tx in raw_transactions
    # 3. Отсеивает все транзакции, не имеющие статус SUCCESS и меньше или равные нулю
    if "SUCCES" in tx and int(tx.split(":")[1]) > 0 ]

# Выводим результат
print("Очищенные транзакции:", cleaned_transactions)
