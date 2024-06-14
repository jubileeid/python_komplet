def minta_float_dalam_rentang():
    while True:
        try:
            # Meminta input dari pengguna
            nilai = float(input("Masukkan nilai antara 0 dan 10: "))
            # Memeriksa apakah nilai dalam rentang yang diinginkan
            if 0 <= nilai <= 10:
                # Jika valid, keluar dari loop
                break
            else:
                print("Nilai tidak dalam rentang. Harap masukkan nilai antara 0 dan 10.")
        except ValueError:
            # Jika terjadi kesalahan (misalnya input bukan nilai float)
            print("Input tidak valid. Harap masukkan nilai float.")
    
    # Mengembalikan nilai yang valid
    return nilai

# Menggunakan fungsi
nilai = minta_float_dalam_rentang()
print(f"Nilai yang Anda masukkan adalah: {nilai}")
