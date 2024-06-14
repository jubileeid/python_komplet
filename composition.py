class Mesin:
    def start(self):
        return "Mesin Menyala!"

class Mobil:
    def __init__(self, brand):
        self.brand = brand
        self.mesin = Mesin()  
        # Komposisi: Mobil memiliki sebuah Mesin

    def start_engine(self):
        return self.mesin.start()  
        # Menggunakan metode start dari Engine

# Contoh penggunaan
mobilsaya = Mobil("Toyota")
print(mobilsaya.start_engine())  # Output: Engine started
