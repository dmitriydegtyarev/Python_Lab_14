import os
import csv
import matplotlib.pyplot as plt

csv_filename = "input_data.csv"

if not os.path.exists(csv_filename):
    print(f"Файл {csv_filename} не знайдено.")
    exit()

indicator_name = "Net migration"
years = list(range(1991, 2025))

year_columns = {year: f"{year} [YR{year}]" for year in years}

country_data = {}

try:
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Фільтруємо рядки по потрібному показнику
            if row["Series Name"] == indicator_name:
                country = row["Country Name"]
                values = []
                # Зчитуємо значення для кожного року
                for year in years:
                    col = year_columns[year]
                    try:
                        value = float(row[col])
                    except (ValueError, KeyError):
                        value = None  # Якщо даних немає або формат невірний
                    values.append(value)
                country_data[country] = values
except Exception as e:
    print("Сталася помилка при зчитуванні даних:", e)
    exit()

# Лінійний графік для України та Канади
selected_countries = ["Ukraine", "Canada"]

plt.figure(figsize=(12, 6))
for country in selected_countries:
    if country in country_data:
        plt.plot(years, country_data[country],
                 linestyle='-',
                 linewidth=2,
                 label=country)
    else:
        print(f"Дані для країни '{country}' відсутні в файлі.")
plt.xlabel("Рік", fontsize=12)
plt.ylabel("Net migration", fontsize=12)
plt.title("Динаміка показника Net migration (1991-2024) для України та Канади", fontsize=14)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Стовпчикова діаграма
print("Доступні країни:")
for name in sorted(country_data.keys()):
    print(name)

user_country = input("Введіть назву країни для побудови стовпчикової діаграми: ").strip()

if user_country in country_data:
    plt.figure(figsize=(12, 6))
    plt.bar(years, country_data[user_country], color='red')
    plt.xlabel("Рік", fontsize=12)
    plt.ylabel("Net migration", fontsize=12)
    plt.title(f"Стовпчикова діаграма Net migration для {user_country} (1991-2024)", fontsize=14)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()
else:
    print(f"Дані для країни '{user_country}' відсутні в файлі.")