import pandas as pd
import matplotlib.pyplot as plt

# 1. Завантаження CSV-файлу
df = pd.read_csv("velodani.csv")

print("\nПерші 5 рядків датафрейму:")
print(df.head())

print("\nІнформація про датафрейм:")
print(df.info())

print("\nОписова статистика:")
print(df.describe())


# 2. Перетворюємо колонку з датою у формат дати
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

# Видаляємо порожню колонку з часом (Unnamed: 1)
df = df.drop(columns=["Unnamed: 1"])


# 3. Загальна кількість велосипедистів за рік на усіх велодоріжках
total_all_tracks = df[["Berri1", "Maisonneuve_1", "Maisonneuve_2", "Brébeuf"]].sum().sum()

print("\nЗагальна кількість велосипедистів за рік на усіх велодоріжках:")
print(total_all_tracks)


# 4. Загальна кількість велосипедистів за рік на кожній велодоріжці
total_by_track = df[["Berri1", "Maisonneuve_1", "Maisonneuve_2", "Brébeuf"]].sum()

print("\nЗагальна кількість велосипедистів за рік по кожній велодоріжці:")
print(total_by_track)


# 5. Додаємо колонку з місяцем
df["Місяць"] = df["Date"].dt.month


# 6. Визначаємо найпопулярніший місяць для трьох велодоріжок
tracks = ["Berri1", "Maisonneuve_1", "Maisonneuve_2"]

for track in tracks:
    monthly_sum = df.groupby("Місяць")[track].sum()
    best_month = monthly_sum.idxmax()

    print(f"\nНайпопулярніший місяць для доріжки {track}: {best_month}")
    print(monthly_sum)


# 7. Графік завантаженості однієї велодоріжки (наприклад Berri1)
monthly_berri = df.groupby("Місяць")["Berri1"].sum()

plt.figure()
monthly_berri.plot()
plt.title("Завантаженість велодоріжки Berri1 по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)
plt.show()
