# Načtení dat ze souboru
data = []
with open('AAPL.csv', 'r') as file:
    for line in file:
        if line.startswith('Date'):
            continue  # Přeskočení řádku s hlavičkou
        parts = line.strip().split(',')
        data.append(parts)

# Nalezení nejvyšší a nejnižší ceny akcií a jejich datumu
max_price = float(data[0][2])
min_price = float(data[0][3])
max_date = data[0][0]
min_date = data[0][0]

for row in data:
    high = float(row[2])
    low = float(row[3])
    date = row[0]

    if high > max_price:
        max_price = high
        max_date = date

    if low < min_price:
        min_price = low
        min_date = date

# Výpočet průměrné ceny Close
total_close = sum([float(row[4]) for row in data])
average_price = total_close / len(data)

# Výpis výsledků
print(f"Nejvyšší cena byla {max_price} dne {max_date}")
print(f"Nejnižší cena byla {min_price} dne {min_date}")
print(f"Průměrná cena byla {average_price}")
