class Royalti:
    def __init__(self, harga, eksemplar):
        self.__royalti = 15/100
        self.harga = harga
        self.eksemplar = eksemplar
    
    def get_royalti(self):
        return self.__royalti
    
    def set_royalti(self, royalti):
        self.__royalti = royalti / 100

    def hitung_royalti(self):
        return self.__royalti * self.harga * self.eksemplar
    
my_royalti = Royalti(75000, 2000)
# menggunakan getter
print(f"Persentase royalti: {my_royalti.get_royalti()}")
print(f"Royalti saya sebesar {my_royalti.hitung_royalti()}")

# menggunakan setter
my_royalti.set_royalti(10)
print(f"Besaran royalti: {my_royalti.get_royalti()}")
print(f"Royalti saya sebesar {my_royalti.hitung_royalti()}")




        