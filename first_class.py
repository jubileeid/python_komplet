# Fungsi untuk dihitung
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# Fungsi yang menerima fungsi lain sebagai argumen
def operate(func, a, b):
    return func(a, b)

# Menyimpan fungsi dalam variabel
operation = multiply
result = operation(5, 3)
print(f"Hasil multiply: {result}")

# Menggunakan fungsi sebagai argumen
result_add = operate(add, 10, 5)
result_multiply = operate(multiply, 10, 5)
print(f"Hasil add: {result_add}")
print(f"Hasil multiply: {result_multiply}")

# Mengembalikan fungsi dari fungsi lain
def get_operator(operator):
    if operator == 'add':
        return add
    elif operator == 'multiply':
        return multiply
    else:
        return None

# Menggunakan fungsi yang dikembalikan
selected_operation = get_operator('add')
if selected_operation:
    result = selected_operation(7, 3)
    print(f"Hasil operasi yang dipilih (add): {result}")

selected_operation = get_operator('multiply')
if selected_operation:
    result = selected_operation(7, 3)
    print(f"Hasil operasi yang dipilih (multiply): {result}")
