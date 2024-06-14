from datetime import datetime, timedelta

# Fungsi untuk menghitung tabungan setelah setahun dengan bunga 5% per tahun
def hitung_tabungan_awal(tabungan_awal):
    # Tanggal sekarang
    tanggal_sekarang = datetime.now()

    # Menambahkan satu tahun ke tanggal sekarang
    tahun_depan = tanggal_sekarang + timedelta(days=365)

    # Menghitung bunga
    bunga = tabungan_awal * 0.05

    # Total tabungan setelah setahun
    total_tabungan = tabungan_awal + bunga

    return total_tabungan

# Menghitung tabungan awal dan tabungan setelah setahun
tabungan_awal = float(input("Masukkan jumlah tabungan awal: "))
tabungan_setahun = hitung_tabungan_awal(tabungan_awal)

# Menampilkan hasil
print(f"Tabungan awal: Rp {tabungan_awal}")
print(f"Tabungan setelah setahun dengan bunga 5%: Rp {tabungan_setahun}")
