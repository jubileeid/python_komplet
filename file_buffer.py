# Membuka file tanpa buffering (mode biner)
with open('contoh_file_biner.txt', 'wb', buffering=0) as file:
    file.write(b"Ini adalah teks biner.")

# Membuka file dengan buffering baris
with open('contoh_file_teks.txt', 'w', buffering=1) as file:
    file.write("Ini adalah baris pertama.\n")
    file.write("Ini adalah baris kedua.\n")
    # Data akan ditulis ke file setelah setiap baris baru ('\n').

# Membuka file dengan ukuran buffer khusus
with open('contoh_file_buffer.txt', 'w', buffering=8) as file:
    file.write("Buffering ukuran 8 byte.\n")
    file.write("Buffering dapat meningkatkan kinerja.\n")
