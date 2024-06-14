class Kendaraan:
    def bergerak(self):
        print("Kendaraan sedang bergerak.")

class Terbang:
    def terbang(self):
        print("Objek sedang terbang.")

class MobilTerbang(Kendaraan, Terbang):
    pass

# Contoh penggunaan
mt = MobilTerbang()
mt.bergerak()  # Output: Kendaraan sedang bergerak.
mt.terbang()   # Output: Objek sedang terbang.
