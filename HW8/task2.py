
import time
from typing import Callable, Any, Tuple

# Константы для расчетов, задала в начале как по инструкции
MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0




# ==========================================
# Задание 2. Декораторы и Lambda
# ==========================================
def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор: замеряет, сколько секунд выполнялась функция,
    и выводит имя функции в консоль.

    Args:
        func (Callable[..., Any]): Функция, которую необходимо обернуть и замерить.

    Returns:
        Callable[..., Any]: Обернутая функция (wrapper), выполняющая замеры времени.
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
    """Сортируем список жанров по выручке (total_sales) от большего к меньшему.

    Args:
        genre_sales (list[dict[str, str | float]]): Список словарей с данными о продажах жанров.

    Returns:
        list[dict[str, str | float]]: Новый отсортированный по убыванию выручки список жанров.
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

run_task_2_tests()
