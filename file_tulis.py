# Menulis teks menggunakan write()
with open('contoh_teks.txt', 'w') as file:
    file.write("Ini adalah baris pertama.\n")
    file.write("Ini adalah baris kedua.\n")

# Menulis beberapa baris teks menggunakan writelines()
with open('contoh_teks.txt', 'a') as file:  # 'a' untuk append
    baris_baru = ["Ini adalah baris ketiga.\n", "Ini adalah baris keempat.\n"]
    file.writelines(baris_baru)

# Membaca kembali isi file untuk verifikasi
with open('contoh_teks.txt', 'r') as file:
    isi_file = file.read()
    print(isi_file)
