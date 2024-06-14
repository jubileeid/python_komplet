# Membuat beberapa variabel
x = [1, 2, 3]
y = "hello"
z = 3.14

# Mendapatkan alamat memori dari masing-masing objek
alamat_memori_x = id(x)
alamat_memori_y = id(y)
alamat_memori_z = id(z)

# Mencetak alamat memori dari masing-masing objek
print(f'Alamat memori dari x: {alamat_memori_x}')
print(f'Alamat memori dari y: {alamat_memori_y}')
print(f'Alamat memori dari z: {alamat_memori_z}')
