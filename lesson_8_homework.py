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


# ==========================================
# Задание 2. Декораторы и Lambda
# ==========================================
def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор: замеряет, сколько секунд выполнялась функция,
    и выводит имя функции в консоль.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()  # засекаем время старта

        result = func(*args, **kwargs)  # выполняем саму функцию

        end_time = time.perf_counter()  # засекаем время конца
        execution_time = round(end_time - start_time, TIME_DECIMALS)

        # Вывод лога по заданию
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {execution_time} сек.")
        return result

    return wrapper


@performance_logger
def get_sorted_report(genre_sales: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """
    Сортируем список жанров по выручке (total_sales) от большего к меньшему.
    """
    # Использую sorted с лямбдой, чтобы вытащить значение выручки из словаря
    return sorted(genre_sales, key=lambda item: item["total_sales"], reverse=True)


def run_task_2_tests() -> None:
    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

    set_1 = [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55}
    ]

    set_2 = [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00}
    ]

    set_3 = [
        {"category": "Drama", "total_sales": 500.00}
    ]

    test_sets = [set_1, set_2, set_3]

    for i, data_set in enumerate(test_sets, start=1):
        print(f"ТЕСТ {i}")
        sorted_data = get_sorted_report(data_set)
        print("Топ категорий по выручке:")
        for idx, row in enumerate(sorted_data, start=1):
            print(f"{idx}. {row['category']}: {row['total_sales']}")
    print()

# ==========================================
# Задание 3. Обработка ошибок (try-except-finally)
# ==========================================
def calculate_overdue_fine(movie_title: str, days_overdue: Any, fine_rate: float) -> tuple[float, float] | None:
    """
    Считаем штраф за просрочку и индекс возврата.
    Тут защищаемся от кривых данных с помощью try-except.
    """
    try:
        # Пробуем перевести дни в число с плавающей точкой
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{movie_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index

    except ValueError as e:
        # Если ввели текст вместо числа (например, "пять")
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': {e}")
    except ZeroDivisionError as e:
        # Если просрочка 0 дней, на ноль делить нельзя
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': {e}")
    except TypeError as e:
        # Если прилетел вообще не тот тип (например, список)
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{movie_title}': {e}")
    finally:
        # Этот блок сработает всегда, была ошибка или нет
        print("Проверка транзакции возврата завершена")

    return None


def run_task_3_tests() -> None:
    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

    calculate_overdue_fine("Matrix", 5, 1.5)  # ОК
    calculate_overdue_fine("Inception", "пять", 2.0)  # ValueError
    calculate_overdue_fine("Avatar", 0, 2.5)  # ZeroDivisionError
    calculate_overdue_fine("Interstellar", [3], 3.0)  # TypeError
    print()


# Запуск всех тестов при старте скрипта
if __name__ == "__main__":
    run_task_1_tests()
    run_task_2_tests()
    run_task_3_tests()