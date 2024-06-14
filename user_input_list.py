def minta_nilai():
    # List kosong untuk menyimpan nilai
    nilai_list = []
    
    # Menentukan jumlah nilai yang akan dimasukkan
    jumlah_nilai = int(input("Masukkan jumlah nilai yang akan dimasukkan: "))
    
    # Meminta input nilai dari pengguna
    for i in range(jumlah_nilai):
        while True:
            try:
                # Meminta input dari pengguna dan konversi ke float
                nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
                # Menambahkan nilai ke dalam list
                nilai_list.append(nilai)
                # Keluar dari loop jika input valid
                break
            except ValueError:
                # Menangani kesalahan jika input tidak valid
                print("Input tidak valid. Harap masukkan nilai berupa angka.")
    
    return nilai_list

def hitung_rata_rata(nilai_list):
    # Menghitung rata-rata dari nilai dalam list
    jumlah_nilai = len(nilai_list)
    total_nilai = sum(nilai_list)
    rata_rata = total_nilai / jumlah_nilai if jumlah_nilai > 0 else 0
    return rata_rata

# Menggunakan fungsi
nilai_list = minta_nilai()
rata_rata = hitung_rata_rata(nilai_list)

print(f"Nilai yang Anda masukkan: {nilai_list}")
print(f"Rata-rata nilai: {rata_rata:.2f}")
