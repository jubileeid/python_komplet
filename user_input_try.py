def minta_bilangan_bulat():
    while True:
        try:
            # Meminta input dari pengguna
            angka = int(input("Masukkan bilangan bulat: "))
            # Jika berhasil, keluar dari loop
            break
        except ValueError:
            # Jika terjadi kesalahan (misalnya input bukan bilangan bulat)
            print("Input tidak valid. Harap masukkan bilangan bulat.")
    
    # Mengembalikan nilai bilangan bulat yang valid
    return angka

# Menggunakan fungsi
bilangan = minta_bilangan_bulat()
print(f"Bilangan bulat yang Anda masukkan adalah: {bilangan}")
