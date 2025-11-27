import matplotlib.pyplot as plt
import csv


# 1. Зчитування даних з CSV

years = []      # роки
ukraine_pop = []  # населення України
usa_pop = []      # населення США

with open('dani.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # перший рядок - заголовки
    years = [int(h.split()[0]) for h in header[4:]]  # роки з заголовків

    for row in reader:
        country = row[2]
        data = row[4:4 + len(years)]
        data = [int(x) if x != '' else 0 for x in data]
        if country == "Ukraine":
            ukraine_pop = data
        elif country == "United States":
            usa_pop = data

print("Роки:", years)
print("Населення України:", ukraine_pop)
print("Населення США:", usa_pop)


# Масиви у мільйонах
ukraine_pop_mln = [x / 1_000_000 for x in ukraine_pop]
usa_pop_mln = [x / 1_000_000 for x in usa_pop]

# Лінійний графік
plt.plot(years, ukraine_pop_mln, label='Ukraine', color='blue', linewidth=2)
plt.plot(years, usa_pop_mln, label='USA', color='red', linewidth=2)
plt.title('Population Dynamics (2005–2024)', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (millions)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()



# Стовпчаста діаграма для країни, введеної користувачем

country_input = input("Введіть назву країни (Ukraine або United States): ").strip()

if country_input == "Ukraine":
    data_to_plot = ukraine_pop_mln
elif country_input == "United States":
    data_to_plot = usa_pop_mln
else:
    print("Невідома країна!")
    exit()

plt.bar(years, data_to_plot, color='green')
plt.title(f'Population of {country_input} (2005–2024)', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (millions)', fontsize=12)

# Підписи над стовпцями
for i, v in enumerate(data_to_plot):
    plt.text(years[i], v + 0.5, f"{v:.1f}", ha='center', fontsize=8)

plt.show()

