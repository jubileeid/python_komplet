class Pegawai:
    def __init__(self, nama, gaji_dasar):
        self.nama = nama
        self._gaji_dasar = gaji_dasar

    def hitung_gaji(self):
        return self._gaji_dasar

class Manajer(Pegawai):
    def __init__(self, nama, gaji_dasar, tunjangan):
        super().__init__(nama, gaji_dasar)
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self._gaji_dasar + self.tunjangan

# Contoh penggunaan
pegawai1 = Pegawai("pegawai1", 5000000)
print(f"Gaji Pegawai 1: {pegawai1.hitung_gaji()}")

manajer1 = Manajer("manajer1", 7000000, 3000000)
print(f"Gaji Manajer 1: {manajer1.hitung_gaji()}")