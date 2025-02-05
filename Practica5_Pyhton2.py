import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Leer el archivo CSV
file_path = "C:/Users/Miguel Gómez/Desktop/Universidad/MASTER/Ciclo de vida de los datos/practica workflow/Forbes.csv"

earnings_by_year = defaultdict(list)

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            year = int(row['Year'])
            earnings = float(row['earnings ($ million)'])
            earnings_by_year[year].append(earnings)
        except ValueError:
            continue  # Saltar filas con valores no válidos

# Calcular la media de ganancias por año
mean_earnings_by_year = {year: sum(earnings) / len(earnings) for year, earnings in earnings_by_year.items()}

# Ordenar por año
sorted_years = sorted(mean_earnings_by_year.keys())
sorted_earnings = [mean_earnings_by_year[year] for year in sorted_years]

# Graficar la evolución temporal de las ganancias
plt.plot(sorted_years, sorted_earnings, marker='o')
plt.xlabel('Year')
plt.ylabel('Mean earnings ($ million)')
plt.title('Temporal Analysis of the Earnings of the Top 10 Athletes per Year')
plt.grid()
plt.savefig('Top10EarningsPerYear.png')
plt.show()
