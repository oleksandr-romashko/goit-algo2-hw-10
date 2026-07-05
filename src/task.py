"""Greedy algorithm for university class scheduling (set cover problem)."""


class Teacher:
    """Represents a teacher with their personal info and teachable subjects."""

    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    """
    Assign teachers to subjects using a greedy set-cover approach.

    At each step selects the teacher who covers the most uncovered subjects.
    Ties are broken by age (youngest first).
    Returns a list of selected Teacher instances with assigned_subjects set,
    or None if full coverage is impossible.
    """
    uncovered = set(subjects)
    remaining = list(teachers)
    schedule = []

    while uncovered:
        best_teacher = None
        best_coverage = set()

        for teacher in remaining:
            coverage = teacher.can_teach_subjects & uncovered
            if not coverage:
                continue
            if (len(coverage) > len(best_coverage) or
                    (len(coverage) == len(best_coverage) and
                     teacher.age < best_teacher.age)):
                best_teacher = teacher
                best_coverage = coverage

        if best_teacher is None:
            return None

        best_teacher.assigned_subjects = best_coverage
        schedule.append(best_teacher)
        remaining.remove(best_teacher)
        uncovered -= best_coverage

    return schedule


if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com',
                {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 35, 'm.petrenko@example.com',
                {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com',
                {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com',
                {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com',
                {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com',
                {'Біологія'}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, "
                  f"{teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
