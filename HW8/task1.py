import time
from typing import Callable, Any, Tuple

# Константы для расчетов, задала в начале как по инструкции
MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0


# ==========================================
# Задание 1. Расчет оптовой аренды
# ==========================================
def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Считаю общую сумму заказа с учетом скидки и смотрю,
    превышает ли она наш лимит (MAX_RENTAL_BATCH_LIMIT).

    Args:
        quantity (int): Количество единиц товара в заказе.
        rental_rate (float): Ставка аренды за единицу.
        discount (float): Размер скидки (по умолчанию 0.0).

    Returns:
        tuple[float, bool]: Итоговая сумма заказа и признак превышения лимита.
    """
    # Считаем сумму и сразу округляем до 2 знаков после запятой
    final_sum = round(quantity * rental_rate * (1.0 - discount), 2)

    # Проверяем, нужен ли ручной менеджер (если сумма больше 150)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded


def run_task_1_tests() -> None:
    # Проверяем работу функции на разных партиях дисков
    print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

    # Вызов с позиционными аргументами
    sum_1, exceeded_1 = calculate_rental_batch(30, 2.99)
    print(f"Партия 1 (Academy Dinosaur): Сумма {sum_1}$. Превышение лимита: {exceeded_1}")

    # Вызов с именованными аргументами и скидкой 10%
    sum_2, exceeded_2 = calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.1)
    print(f"Партия 2 (Affair Prejudice): Сумма {sum_2}$. Превышение лимита: {exceeded_2}")

    sum_3, exceeded_3 = calculate_rental_batch(10, 1.99)
    print(f"Партия 3 (Agent Truman): Сумма {sum_3}$. Превышение лимита: {exceeded_3}")

    sum_4, exceeded_4 = calculate_rental_batch(quantity=50, rental_rate=3.50, discount=0.2)
    print(f"Партия 4 (African Egg): Сумма {sum_4}$. Превышение лимита: {exceeded_4}")
    print()

run_task_1_tests()
