# Membuat contoh file teks
with open('contoh.txt', 'w') as file:
    file.write("Baris pertama.\nBaris kedua.\nBaris ketiga.\n")

# Membaca seluruh isi file dengan read()
with open('contoh.txt', 'r') as file:
    isi_file = file.read()
    print("Membaca seluruh isi file dengan read():")
    print(isi_file)

# Membaca file baris per baris dengan readline()
with open('contoh.txt', 'r') as file:
    print("Membaca file baris per baris dengan readline():")
    while True:
        baris = file.readline()
        if not baris:
            break
        print(baris, end='')

# Membaca semua baris dan mengembalikannya sebagai list dengan readlines()
with open('contoh.txt', 'r') as file:
    semua_baris = file.readlines()
    print("\nMembaca semua baris dengan readlines():")
    print(semua_baris)

# Menggunakan iterator untuk membaca file baris demi baris
with open('contoh.txt', 'r') as file:
    print("Membaca file baris demi baris menggunakan iterator:")
    for baris in file:
        print(baris, end='')
