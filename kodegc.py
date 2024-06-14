import gc

# Memaksa garbage collector untuk berjalan
collected = gc.collect()
print(f"Garbage collector: Mengumpulkan {collected} objects.")

# Menonaktifkan garbage collector otomatis
gc.disable()
print("Garbage collector telah disabled.")

# Mengaktifkan kembali garbage collector otomatis
gc.enable()
print("Garbage collector kini enabled.")

# Mendapatkan statistik pengumpulan sampah
print(gc.get_stats())