from typing import List


# Базовый класс учащегося (из предыдущей части урока)
class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name: str = name
        self.surname: str = surname
        self.score: int = score
        self.passing_grade: int = passing_grade

    def visit_lecture(self) -> None:
        """Имитирует посещение лекции, увеличивая баллы на 1."""
        self.score += 1

    def do_homework(self) -> None:
        """Выполнение обычной домашней работы (+1 балл)."""
        self.score += 1

    def is_passing(self) -> bool:
        """Проверяет, проходит ли студент курс по порогу баллов."""
        return self.score >= self.passing_grade


# 1. Класс HardworkingTrainee (наследник Trainee)
class HardworkingTrainee(Trainee):
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2


# 1. Класс AuditTrainee (наследник Trainee)
class AuditTrainee(Trainee):
    def is_passing(self) -> bool:
        """Вольнослушатели всегда считаются успешно прошедшими курс."""
        return True


# 2. Класс Cohort (Учебная группа) - Композиция / Агрегация
class Cohort:
    def __init__(self, title: str):
        self.title: str = title
        self.trainees: List[Trainee] = []

    def add_trainee(self, trainee: Trainee) -> None:
        """Добавляет учащегося в группу."""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Имитирует проведение лекции — вызов visit_lecture() (полиморфизм)."""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> List[Trainee]:
        """Возвращает список учащихся группы, у которых is_passing() возвращает True."""
        return [trainee for trainee in self.trainees if trainee.is_passing()]


# ==========================================
# Входные данные и тесты из задания
# ==========================================

# # 1. Создаем учащихся разных типов
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

# # 2. Создаем группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

# # 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()

# # 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()

# # 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")

print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")