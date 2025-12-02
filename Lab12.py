import pandas as pd
import matplotlib.pyplot as plt
import os

# ФУНКЦІЯ СТВОРЕННЯ CSV-ФАЙЛУ
def create_csv_file(filename):
    data = {
        "Дата": [
            "2024-01-01", "2024-01-02", "2024-01-03",
            "2024-01-01", "2024-01-02", "2024-01-03",
            "2024-01-01", "2024-01-02", "2024-01-03"
        ],
        "Назва": [
            "Долар", "Долар", "Долар",
            "Apple", "Apple", "Apple",
            "Продажі", "Продажі", "Продажі"
        ],
        "Значення": [
            38.0, 38.2, 38.5,
            180, 182, 185,
            250, 270, 300
        ],
        "Тип": [
            "Валюта", "Валюта", "Валюта",
            "Акція", "Акція", "Акція",
            "Продажі", "Продажі", "Продажі"
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(" CSV-файл успішно створено!")


# ФУНКЦІЯ ЗАВАНТАЖЕННЯ ДАНИХ
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print(" Дані успішно завантажено!")
        return df
    except FileNotFoundError:
        print(" Помилка: Файл не знайдено!")
        return None


# ФУНКЦІЯ МЕНЮ
def show_menu():
    print("\nОберіть тип аналізу:")
    print("1 - Динаміка валют")
    print("2 - Динаміка акцій")
    print("3 - Динаміка продажів")
    print("0 - Вихід")


# ФУНКЦІЯ ПОБУДОВИ ГРАФІКА
def plot_data(df, choice):
    if choice == 1:
        filtered = df[df["Тип"] == "Валюта"]
        title = "Динаміка валют"
        filename_img = "currency_chart.png"
        filename_txt = "currency_result.txt"
    elif choice == 2:
        filtered = df[df["Тип"] == "Акція"]
        title = "Динаміка акцій"
        filename_img = "stock_chart.png"
        filename_txt = "stock_result.txt"
    elif choice == 3:
        filtered = df[df["Тип"] == "Продажі"]
        title = "Динаміка продажів"
        filename_img = "sales_chart.png"
        filename_txt = "sales_result.txt"
    else:
        print(" Невірний вибір!")
        return

    # Побудова графіка
    plt.figure()
    for name in filtered["Назва"].unique():
        data = filtered[filtered["Назва"] == name]
        plt.plot(data["Дата"], data["Значення"], label=name)

    plt.title(title)
    plt.xlabel("Дата")
    plt.ylabel("Значення")
    plt.legend()
    plt.grid(True)

    # Збереження графіка у PNG
    plt.savefig(filename_img)
    plt.show()

    # Збереження результатів у TXT
    filtered.to_csv(filename_txt, index=False, sep=';')

    print(f" Графік збережено у файл: {filename_img}")
    print(f" Дані збережено у файл: {filename_txt}")


# ГОЛОВНА ФУНКЦІЯ
def main():
    filename = "financial_data.csv"

    print(" Програма аналізу фінансових даних")

    # Якщо файл не існує — створити його
    if not os.path.exists(filename):
        create_csv_file(filename)

    df = load_data(filename)
    if df is None:
        return

    while True:
        show_menu()

        try:
            choice = int(input("Ваш вибір: "))
        except ValueError:
            print(" Помилка: введено не число!")
            continue

        if choice == 0:
            print(" Завершення роботи програми.")
            break
        elif choice in [1, 2, 3]:
            plot_data(df, choice)
        else:
            print(" Невірний пункт меню!")

main()
