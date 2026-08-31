import time
from typing import Callable, Any, Tuple

# Константы для расчетов, задала в начале как по инструкции
MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0

# ==========================================
# Задание 3. Обработка ошибок (try-except-finally)
# ==========================================
def calculate_overdue_fine(movie_title: str, days_overdue: Any, fine_rate:float) -> tuple[float, float] | None:
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
    calculate_overdue_fine("Interstellar", [3], 3.0)


run_task_3_tests()