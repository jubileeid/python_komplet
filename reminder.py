import time

def reminder_minum_air():
    while True:
        # Mendapatkan waktu saat ini
        waktu_sekarang = time.localtime()
        
        # Memeriksa apakah sudah jam 1 menit ke setiap jam
        if waktu_sekarang.tm_min == 1:
            print("Sudah satu jam, minum air!")
            # Tunggu 5 detik sebelum melanjutkan (opsional)
            time.sleep(5)
        
        # Tunggu 1 menit sebelum memeriksa lagi
        time.sleep(60)

# Jalankan fungsi reminder_minum_air
reminder_minum_air()
