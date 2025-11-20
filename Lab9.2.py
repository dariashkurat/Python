import json
import os

#   1. ПЕРВИННІ ДАНІ ДЛЯ JSON

initial_trains = [
    {"номер": "701", "маршрут": "Київ – Харків",     "прибуття": "10:15", "відправлення": "10:30"},
    {"номер": "112", "маршрут": "Львів – Полтава",   "прибуття": "09:40", "відправлення": "09:55"},
    {"номер": "350", "маршрут": "Одеса – Суми",      "прибуття": "12:05", "відправлення": "12:20"},
    {"номер": "90",  "маршрут": "Харків – Київ",     "прибуття": "14:00", "відправлення": "14:10"},
    {"номер": "45",  "маршрут": "Дніпро – Львів",    "прибуття": "08:30", "відправлення": "08:50"},
    {"номер": "801", "маршрут": "Запоріжжя – Київ",  "прибуття": "16:25", "відправлення": "16:45"},
    {"номер": "703", "маршрут": "Київ – Кривий Ріг", "прибуття": "17:00", "відправлення": "17:15"},
    {"номер": "17",  "маршрут": "Чернігів – Одеса",  "прибуття": "19:50", "відправлення": "20:05"},
    {"номер": "55",  "маршрут": "Київ – Ужгород",    "прибуття": "06:10", "відправлення": "06:25"},
    {"номер": "14",  "маршрут": "Харків – Львів",    "прибуття": "21:30", "відправлення": "21:45"}
]



#   СТВОРЕННЯ JSON, якщо його немає

if not os.path.exists("trains.json"):
    with open("trains.json", "w", encoding="utf-8") as f:
        json.dump(initial_trains, f, ensure_ascii=False, indent=4)


def load_data():
    with open("trains.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open("trains.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



#   1. Переглянути дані
def view_trains():
    trains = load_data()
    print("\nВСІ ПОЇЗДИ:")
    for t in trains:
        print(t)

#   2. Додати або видалити поїзд
def add_or_delete():
    trains = load_data()

    print("\n1 – Додати поїзд")
    print("2 – Видалити поїзд")
    choice = input("Ваш вибір: ")

    if choice == "1":
        num = input("Номер поїзда: ")
        route = input("Маршрут: ")
        arr = input("Час прибуття (ГГ:ХХ): ")
        dep = input("Час відправлення (ГГ:ХХ): ")

        trains.append({
            "номер": num,
            "маршрут": route,
            "прибуття": arr,
            "відправлення": dep
        })

        save_data(trains)
        print("Поїзд додано!")

    elif choice == "2":
        num = input("Введіть номер поїзда для видалення: ")
        new_list = [t for t in trains if t["номер"] != num]

        if len(new_list) == len(trains):
            print("Такого поїзда немає!")
        else:
            save_data(new_list)
            print("Поїзд видалено.")
    else:
        print("Невірний вибір.")


#   3. Пошук поїзда за номером або маршрутом
def search_trains():
    trains = load_data()
    text = input("\nВведіть номер або частину маршруту: ").lower()

    found = [t for t in trains if text in t["номер"].lower() or text in t["маршрут"].lower()]

    if found:
        print("\nЗНАЙДЕНІ ПОЇЗДИ:")
        for f in found:
            print(f)
    else:
        print("Нічого не знайдено.")


#   4. Знайти поїзди, що стоять у введений час
def trains_on_station():
    trains = load_data()

    try:
        h = int(input("Година (0–23): "))
        m = int(input("Хвилини (0–59): "))
    except ValueError:
        print("Некоректне введення!")
        return

    t_min = h * 60 + m
    found = []

    for t in trains:
        ah, am = map(int, t["прибуття"].split(":"))
        dh, dm = map(int, t["відправлення"].split(":"))

        if ah * 60 + am <= t_min <= dh * 60 + dm:
            found.append(t)

    if found:
        print("\nПОЇЗДИ НА СТАНЦІЇ:")
        for f in found:
            print(f"Поїзд", f["номер"], "|", f["маршрут"])
    else:
        print("У цей час поїздів немає.")


#   ГОЛОВНЕ МЕНЮ (1–5)

while True:
    print("\n" + "-" * 50)
    print("1 - Переглянути дані")
    print("2 - Додати новий поїзд (видалити)")
    print("3 - Пошук поїздів (номер або маршрут)")
    print("4 - Знайти поїзди, які стоять у введений час")
    print("5 - Вийти")
    print("-" * 50)

    choice = input("Введіть пункт меню: ")

    if choice == "1":
        view_trains()
    elif choice == "2":
        add_or_delete()
    elif choice == "3":
        search_trains()
    elif choice == "4":
        trains_on_station()
    elif choice == "5":
        print("Вихід...")
        break
    else:
        print("Неправильний вибір!")
