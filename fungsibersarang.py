def outer_function(text):
    def inner_function():
        print(text)
    return inner_function

# Menggunakan fungsi bersarang
closure_function = outer_function("Hello from the inner function!")
closure_function()
