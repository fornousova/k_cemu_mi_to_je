# jednoduchá analýza historie akcii firem
# pro slozitejší finanční analýzy už je potřeba pokročilejšímodely strojového učení nebo jiné modely časových řad
# tento program vezme soubor dat obsahující informace o akcii určité firmy a zjistí kdy byly měly akcie nejvyšší cenu, kdy nejmenší nebo např. jaká je jejich průměrná cena
# data jsme stáhli z internetu a jako příklad tu máme 3 firmy v období od začátku roku 2020 až do současnosti
# Otevření souboru pro čtení
with open("AAPL.csv", "r") as file:
    lines = file.readlines()

# Inicializace proměnných pro nejvyšší a nejnižší cenu a datum
max_price = 0
min_price = float("inf")
max_price_date = ""
min_price_date = ""
total_price = 0
count = 0

# Iterace přes řádky s daty
for line in lines[1:]:  # Přeskočení prvního řádku s hlavičkou
    data = line.strip().split(",")
    date = data[0]
    high = float(data[2])
    low = float(data[3])
    close = float(data[4])  # Přidáme cenu zavření (close)

    # Kontrola nejvyšší ceny
    if high > max_price:
        max_price = high
        max_price_date = date

    # Kontrola nejnižší ceny
    if low < min_price:
        min_price = low
        min_price_date = date

    # Sčítání cen pro výpočet průměru
    total_price += close
    count += 1

# Výpočet průměrné ceny
average_price = total_price / count

# Výpočet maximálního výkyvu
price_range = max_price - min_price

# Výstup s výsledky
print(f"Nejvyšší cena: {max_price} USD byla dosažena dne {max_price_date}")
print(f"Nejnižší cena: {min_price} USD byla dosažena dne {min_price_date}")
print(f"Průměrná cena akcií: {average_price:.2f} USD")
print(f"Maximální výkyv cen: {price_range:.2f} USD")
