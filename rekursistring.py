def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Contoh penggunaan
print(reverse_string("Halo Dunia"))
