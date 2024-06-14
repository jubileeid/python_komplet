class Royalti:
    def __init__(self, harga, eksemplar):
        self.__royalti = 15/100
        self.harga = harga
        self.eksemplar = eksemplar
    
    def hitung_royalti(self):
        return self.__royalti * self.harga * self.eksemplar
    
my_royalti = Royalti(75000, 2000)
print(f"Royalti saya sebesar {my_royalti.hitung_royalti()}")


        