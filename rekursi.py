def sum_recursive(n):
    # Base case: jika n adalah 1, kembalikan nilai 1
    if n == 1:
        return 1
    
    # Recursive case: n + sum_recursive(n - 1)
    else:
        return n + sum_recursive(n - 1)

# Contoh penggunaan
print(sum_recursive(5))

