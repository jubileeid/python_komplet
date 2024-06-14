import sys

# Membuat sebuah list
a = []
print(sys.getrefcount(a))  
# Output: 2 (satu referensi dari 'a', satu dari argumen getrefcount)

# Membuat referensi lain ke list yang sama
b = a
print(sys.getrefcount(a))  
# Output: 3 (referensi dari 'a', 'b', dan argumen getrefcount)

# Menghapus satu referensi
del b
print(sys.getrefcount(a))  
# Output: 2 (referensi dari 'a' dan argumen getrefcount)

# Menghapus semua referensi
del a
# Pada titik ini, objek list tidak memiliki referensi dan akan dikumpulkan oleh garbage collector
