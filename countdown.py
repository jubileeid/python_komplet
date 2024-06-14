import turtle
import time
from datetime import datetime, timedelta

# Fungsi untuk menampilkan teks pada layar turtle
def tampilkan_teks(teks):
    turtle.clear()
    turtle.write(teks, align="center", font=("Arial", 48, "normal"))

# Fungsi untuk menghitung mundur dari waktu yang ditentukan
def hitung_mundur(detik):
    waktu_akhir = datetime.now() + timedelta(seconds=detik)
    while True:
        waktu_tersisa = waktu_akhir - datetime.now()
        if waktu_tersisa.total_seconds() > 0:
            menit, detik = divmod(waktu_tersisa.seconds, 60)
            waktu_str = f"{menit:02}:{detik:02}"
            tampilkan_teks(waktu_str)
            time.sleep(1)
        else:
            tampilkan_teks("Waktu Habis!")
            break

# Setup jendela turtle
turtle.setup(width=600, height=400)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, 0)
turtle.color("red")

# Jalankan hitung mundur selama 1 menit (60 detik)
hitung_mundur(60)

# Menunggu beberapa detik sebelum menutup jendela turtle
time.sleep(5)
turtle.bye()
