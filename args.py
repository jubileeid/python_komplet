def contoh_args_kwargs(*args, **kwargs):
    # Menampilkan semua argumen posisi
    print("Argumen Posisi:")
    for arg in args:
        print(arg)
    
    # Menampilkan semua argumen kata kunci
    print("\nArgumen Kata Kunci:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Memanggil fungsi dengan argumen posisi dan argumen kata kunci
contoh_args_kwargs(1, 2, 3, nama="Alice", umur=30, kota="Jakarta")
