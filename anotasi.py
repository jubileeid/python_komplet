def tambah(a: int, b: int) -> int:
    return a + b

def gabungkan(nama_depan: str, nama_belakang: str) -> str:
    return f"{nama_depan} {nama_belakang}"

def hitung_luas_lingkaran(jari_jari: float) -> float:
    import math
    return math.pi * jari_jari ** 2

# Contoh penggunaan fungsi dengan anotasi tipe
hasil_tambah = tambah(3, 5)
print(f"Hasil tambah: {hasil_tambah}")

nama_lengkap = gabungkan("John", "Doe")
print(f"Nama lengkap: {nama_lengkap}")

luas_lingkaran = hitung_luas_lingkaran(7.5)
print(f"Luas lingkaran: {luas_lingkaran}")
