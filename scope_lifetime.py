# Variabel global
x = "global"

def fungsi_luar():
    # Variabel enclosing
    x = "enclosing"
    
    def fungsi_dalam():
        # Variabel lokal
        x = "local"
        print("Di dalam fungsi_dalam:", x)
    
    fungsi_dalam()
    print("Di dalam fungsi_luar:", x)

fungsi_luar()
print("Di luar semua fungsi:", x)
