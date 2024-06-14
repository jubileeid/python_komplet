# Menulis data biner ke file
data_biner = bytes([120, 3, 255, 0, 100])
with open('contoh_biner.bin', 'wb') as file:
    file.write(data_biner)

# Membaca kembali data biner untuk verifikasi
with open('contoh_biner.bin', 'rb') as file:
    isi_file = file.read()
    print(isi_file)
