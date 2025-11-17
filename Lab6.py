"""
Спільна робота. Третій студент: Шкурат Дар'я Андріївна

Завдання третього студента:
Реалізувати функцію, яка аналізує успішність по предметах:
- обчислює середній бал з кожного предмета по всіх студентах;
- виводить ці середні значення на екран.

Використовується спільний словник students.
"""

# --- словник студентів ---

students = {
    "S001": {
        "group": "КН-43",
        "fio": "Токар Діана Артурівна",
        "course": 2,
        "grades": {
            "Математика": [45, 58, 37],
            "Алгоритми":  [52, 49, 60],
            "Бази даних": [33, 41],
        },
    },
    "S002": {
        "group": "КН-43",
        "fio": "Токар Домініка Артурівна",
        "course": 2,
        "grades": {
            "Математика": [25, 39, 44],
            "Алгоритми":  [51, 46],
            "Бази даних": [40, 42, 38],
        },
    },
    "S003": {
        "group": "КН-43",
        "fio": "Жулавський Матвій Сергійович",
        "course": 2,
        "grades": {
            "Математика": [60, 57],
            "Алгоритми":  [48, 53, 55],
            "Бази даних": [32, 36],
        },
    },
    "S004": {
        "group": "КН-41",
        "fio": "Шкурат Дар'я Андріївна",
        "course": 2,
        "grades": {
            "Математика": [22, 30, 27],
            "Алгоритми":  [34, 28],
            "Бази даних": [19, 26, 31],
        },
    },
}


def avg_overall(grades: dict[str, list[int]]) -> float:
    """Середній бал студента за всіма предметами."""
    total = sum(sum(marks) for marks in grades.values())
    cnt = sum(len(marks) for marks in grades.values())
    return total / cnt if cnt else 0.0


def print_students(db: dict):
    """Короткий вивід студентів і їх середнього балу."""
    print("= Список студентів =")
    for sid, info in db.items():
        avg = avg_overall(info.get("grades", {}))
        print(
            f"[{sid}] {info['fio']} | група {info['group']} | курс {info['course']} "
            f"| середній бал: {avg:.2f}"
        )


def subject_statistics(db: dict):
    """
    Обчислює статистику по предметах:
    - збирає всі оцінки по кожному предмету від усіх студентів;
    - рахує середній бал по предмету;
    - виводить результат на екран.
    """
    subjects_marks: dict[str, list[int]] = {}

    # збираємо всі оцінки по предметах
    for sid, info in db.items():
        grades = info.get("grades", {})
        for subj, marks in grades.items():
            if subj not in subjects_marks:
                subjects_marks[subj] = []
            subjects_marks[subj].extend(marks)

    if not subjects_marks:
        print("Немає даних про предмети.")
        return

    print("\n=== Середній бал по кожному предмету (усі студенти) ===")
    for subj, marks in subjects_marks.items():
        if marks:
            avg = sum(marks) / len(marks)
            print(f"{subj:15s}: середній бал = {avg:.2f} (на основі {len(marks)} оцінок)")
        else:
            print(f"{subj:15s}: немає оцінок")


if __name__ == "__main__":
    print("=== Дані студентів ===")
    print_students(students)

    print()
    subject_statistics(students)

