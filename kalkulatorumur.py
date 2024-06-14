from datetime import datetime

def kalkulator_umur():
    # Meminta pengguna untuk memasukkan tanggal lahir
    tanggal_lahir_str = input("Masukkan tanggal lahir Anda (format: DD-MM-YYYY): ")
    
    # Mengonversi string tanggal lahir menjadi objek datetime
    try:
        tanggal_lahir = datetime.strptime(tanggal_lahir_str, "%d-%m-%Y")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")
        return
    
    # Menghitung usia berdasarkan tanggal lahir
    sekarang = datetime.now()
    usia = sekarang.year - tanggal_lahir.year - ((sekarang.month, sekarang.day) < (tanggal_lahir.month, tanggal_lahir.day))
    
    # Menampilkan usia
    print("Usia Anda adalah:", usia, "tahun.")

# Menjalankan kalkulator umur
kalkulator_umur()
