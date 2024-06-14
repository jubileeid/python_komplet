class PersegiPanjang:
    def __init__(self, panjang, lebar):
        # Attribute instance untuk panjang
        self.panjang = panjang  
        
        # Attribute instance untuk lebar
        self.lebar = lebar      

    def hitung_luas(self):
        # Method untuk menghitung luas
        return self.panjang * self.lebar  

persegipanjang = PersegiPanjang(10,5)

print(f"Panjang: {persegipanjang.panjang} x Lebar: {persegipanjang.lebar} = {persegipanjang.hitung_luas()}")

