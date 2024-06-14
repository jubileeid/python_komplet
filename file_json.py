import json

# Data yang akan ditulis ke file JSON
data = {
    'nama': 'Alice',
    'umur': 30,
    'kota': 'New York',
    'hobi': ['membaca', 'berlari', 'coding']
}

# Menulis data ke file JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Membaca data dari file JSON
with open('data.json', 'r') as file:
    data_dibaca = json.load(file)
    print("Data dari file JSON:")
    print(data_dibaca)
