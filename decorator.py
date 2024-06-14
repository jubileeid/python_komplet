def tes_decorator(func):
    def wrapper():
        print("Selamat Pagi!")
        func()
    return wrapper

@tes_decorator
def halodunia():
    print("Halo Dunia")

halodunia()