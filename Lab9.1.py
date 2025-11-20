import csv

filename = "Exports.csv"

#  1. Відкриваємо файл
try:
    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)

except:
    print(f"Файл не знайдено!")
    exit()

# 2. Знаходимо заголовок
header_index = 0
for i, row in enumerate(rows):
    if "Country Name" in row:
        header_index = i
        break

header = rows[header_index]
data = rows[header_index + 1:]

# 3. Знаходимо індекси потрібних колонок
try:
    col_country = header.index("Country Name")
    col2015 = header.index("2015")
    col2019 = header.index("2019")
except ValueError:
    print("У файлі не знайдено колонок 2015 або 2019!")
    exit()

# 4. Виводимо всі значення
print("Дані за 2015 та 2019 роки ")
for row in data:
    try:
        print(row[col_country], "—", row[col2015], "/", row[col2019])
    except:
        pass

# --- 5. Пошук у діапазоні ---
print("\nТепер виконаємо пошук")
low = input("Введіть нижню межу (%): ")
high = input("Введіть верхню межу (%): ")

try:
    low = float(low)
    high = float(high)
except:
    print("Потрібно вводити числа!")
    exit()

result = []

# 6. Фільтрація
for row in data:
    try:
        val = row[col2019].replace(",", ".")
        if val != "":
            num = float(val)
            if low <= num <= high:
                result.append([row[col_country], row[col2015], row[col2019]])
    except:
        pass

# 7. Запис у файл
with open("Result.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Country", "2015", "2019"])
    writer.writerows(result)

print("\nГотово! Дані записано у Result.csv")
