# Higher-order function yang menerima fungsi sebagai argumen
def apply_function(func, value):
    return func(value)

# Contoh fungsi yang akan diteruskan sebagai argumen
def square(x):
    return x * x

# Menggunakan higher-order function
result = apply_function(square, 5)
print("Hasil apply_function:", result)

# Higher-order function yang mengembalikan fungsi
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# Menggunakan higher-order function untuk membuat fungsi pengali
double = create_multiplier(2)
triple = create_multiplier(3)

print("Double 5:", double(5))
print("Triple 5:", triple(5))
