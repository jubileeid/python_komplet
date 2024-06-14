# Membuka file dalam mode baca ('r')
with open('contoh.txt', 'r') as file:
    # Membaca seluruh isi file
    isi_file = file.read()
    # Menampilkan isi file ke layar
    print("Isi file sebelum ditambahkan teks:")
    print(isi_file)

# Membuka file dalam mode tambah ('a')
with open('contoh.txt', 'a') as file:
    # Menambahkan teks ke file
    file.write("\nTeks tambahan ini ditambahkan pada akhir file.")

# Membuka kembali file dalam mode baca ('r') untuk melihat perubahan
with open('contoh.txt', 'r') as file:
    # Membaca seluruh isi file yang telah diperbarui
    isi_file = file.read()
    # Menampilkan isi file yang telah diperbarui ke layar
    print("\nIsi file setelah ditambahkan teks:")
    print(isi_file)
