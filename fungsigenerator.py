def hitung(maksimal):
    count = 0
    while count < maksimal:
        yield count
        count += 1

# Menggunakan generator
counter = hitung(5)

for num in counter:
    print(num)