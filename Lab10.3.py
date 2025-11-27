import json
import matplotlib.pyplot as plt

# ЗАВАНТАЖЕННЯ ДАНИХ З JSON
with open("trains.json", "r", encoding="utf-8") as f:
    trains = json.load(f)

# ПІДРАХУНОК МІСТ ВІДПРАВЛЕННЯ
cities = {}

for t in trains:
    route = t["маршрут"]
    city = route.split("–")[0].strip()   # беремо місто ДО тире

    if city in cities:
        cities[city] += 1
    else:
        cities[city] = 1

# ФОРМУЄМО ДАНІ ДЛЯ ДІАГРАМИ
labels = list(cities.keys())
values = list(cities.values())

# ПОБУДОВА КРУГОВОЇ ДІАГРАМИ
plt.figure()
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Розподіл поїздів за містами відправлення")
plt.show()
