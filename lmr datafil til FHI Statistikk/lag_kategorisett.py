import csv
import json

# Les inn CSV-filen
atc_data = []
with open('ATC_kode_med_virkestoffnavn.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        if row['atc_verdi'].startswith('A'):  # Filtrer basert på ATC-verdi
            atc_data.append({
                'Label': f"{row['atc_verdi']} - {row['atc_beskrivelse_norsk']}",
                'Value': row['atc_verdi'],
                'Children': []
            })

# Funksjon for å finne riktig plassering for en ATC-kode i hierarkiet
def find_or_create_category(categories, code, label):
    for category in categories:
        if category['Value'] == code:
            return category
    # Hvis kategorien ikke finnes, opprett en ny
    new_category = {'Label': label, 'Value': code, 'Children': []}
    categories.append(new_category)
    return new_category

# Opprett hierarkisk struktur
root_categories = []
for item in atc_data:
    code = item['Value']
    parent = root_categories

    if len(code) > 1:  # Hvis koden har underkategorier
        for level in range(1, len(code)):
            parent_code = code[:level]
            parent_label = f"{parent_code} - "  # Kan utvides med faktisk label hvis nødvendig
            parent = find_or_create_category(parent, parent_code, parent_label)['Children']

    parent.append({'Label': item['Label'], 'Value': item['Value'], 'Children': []})

# Lagre den oppdaterte strukturen til en JSON-fil
output = {
    "TemplateName": "ATC - hierarkisk",
    "Dimension": {
        "Code": "ATC",
        "Label": None,
        "Categories": root_categories
    }
}

with open('atc_kategorisett.json', 'w', encoding='utf-8') as json_file:
    json.dump(output, json_file, ensure_ascii=False, indent=4)
