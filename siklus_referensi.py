import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

# Membuat siklus referensi
a = Node(1)
b = Node(2)
a.ref = b
b.ref = a

# Pada titik ini, meskipun 'a' dan 'b' saling mereferensi, mereka tidak berguna
del a
del b

# Memaksa garbage collector untuk menjalankan pengumpulan siklus
gc.collect()
