class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    # private method untuk menghitung luas
    def __hitung_luas(self):
        return self.panjang * self.lebar
    
    # public method untuk mendapatkan luas
    def get_luas(self):
        return self.__hitung_luas()

# Contoh penggunaan
persegi_panjang1 = PersegiPanjang(10, 5)
print(f"Luas persegi panjang adalah: {persegi_panjang1.get_luas()}")
