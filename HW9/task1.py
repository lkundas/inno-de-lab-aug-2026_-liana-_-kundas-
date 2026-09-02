class Trainee:
    """Класс для учета успеваемости стажера на образовательной платформе."""

    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10) -> None:
        # Инициализируем публичные и приватные атрибуты с аннотацией типов
        self.name: str = name
        self.surname: str = surname
        self.passing_grade: int = passing_grade
        self.__score: int = score  # Приватный атрибут для хранения баллов

    @property
    def score(self) -> int:
        """Геттер для безопасного чтения приватного атрибута __score."""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """Сеттер для валидации и изменения значения баллов."""
        # Проверяем, что входящее значение является целым числом (интом)
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        # Баллы не могут быть отрицательными
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        # Если все проверки пройдены, обновляем значение
        self.__score = value

    def do_homework(self) -> None:
        """Увеличивает score на 1."""
        # Меняем балл через свойство self.score, а не напрямую через __score
        self.score += 1

    def miss_homework(self) -> None:
        """Уменьшает score на 1."""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Увеличивает score на 1."""
        self.score += 1

    def miss_lecture(self) -> None:
        """Уменьшает score на 1."""
        self.score -= 1

    def is_passing(self) -> bool:
        """Возвращает True, если текущий score больше или равен passing_grade, иначе False."""
        return self.score >= self.passing_grade


# Входные данные для тестов:

# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}") 