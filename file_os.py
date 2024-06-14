import os

# Membuat direktori baru
os.mkdir('contoh_direktori')

# Mendaftarkan isi direktori saat ini
isi_direktori = os.listdir('.')
print("Isi direktori saat ini:", isi_direktori)

# Mengganti nama direktori
os.rename('contoh_direktori', 'direktori_baru')

# Menghapus direktori
os.rmdir('direktori_baru')

# Membuat file dan kemudian menghapusnya
with open('contoh_file.txt', 'w') as file:
    file.write("Ini adalah contoh file.")

os.remove('contoh_file.txt')
