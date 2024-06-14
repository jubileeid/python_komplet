# Membuat dua variabel yang merujuk ke objek yang sama
a = [1, 2, 3]
b = a

# Memeriksa apakah a dan b merujuk ke objek yang sama
print(id(a) == id(b))  # Output: True

# Membuat variabel baru yang merujuk ke objek yang berbeda
c = [1, 2, 3]

# Memeriksa apakah a dan c merujuk ke objek yang sama
print(id(a) == id(c))  # Output: False
