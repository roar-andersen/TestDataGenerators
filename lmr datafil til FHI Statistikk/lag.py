import csv
import random
import itertools

# Les ATC-verdier fra filen og legg til 'TOTALT'
with open('atc.txt', 'r') as file:
    atc_values = file.read().splitlines()
atc_values.append('TOTALT')  # Legg til 'TOTALT' for ATC-verdier

# Definer de andre verdiene med 'TOTALT' som en ekstra verdi
age_groups = list(range(0, 22)) + ['TOTALT']  # Aldersgrupper fra 0 til 21 pluss 'TOTALT'
years = list(range(2004, 2024)) + ['TOTALT']  # År fra 2004 til 2023 pluss 'TOTALT'
genders = [0, 1, 2, 'TOTALT']  # Kjønn 0, 1, 2 pluss 'TOTALT'

# Generer alle unike kombinasjoner
combinations = list(itertools.product(atc_values, genders, age_groups, years))

# Skriv til CSV-fil
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    # Skriv kolonneoverskrifter
    csvwriter.writerow(['ATC_Verdi', 'Kjønn_Verdi', 'Aldersgruppe_Verdi', 'År', 'Antall_brukere', 'Brukere_per_1000', 'DDD', 'Flagg'])

    # Skriv data
    for combo in combinations:
        antall_brukere = random.randint(1, 10000)  # Tilfeldig heltall mellom 1 og 10000
        brukere_per_1000 = antall_brukere / 20
        flagg = 0 if antall_brukere > 10 else 1  # Bestem flaggverdi basert på antall_brukere
        if flagg == 1:
            antall_brukere = 0
            brukere_per_1000 = 0
        
        ddd = random.randint(0, 1000)  # Tilfeldig Antall_DDD
        csvwriter.writerow(list(combo) + [antall_brukere, brukere_per_1000, ddd, flagg])

print("CSV-filen 'data.csv' er generert.")
