import pickle

# Data struktural yang akan disimpan
data_struktural = {'nama': 'Alice', 'usia': 30, 'pekerjaan': 'Engineer'}

# Menyimpan data struktural ke file
with open('data.pickle', 'wb') as file:
    pickle.dump(data_struktural, file)

# Membaca kembali data struktural untuk verifikasi
with open('data.pickle', 'rb') as file:
    data_terbaca = pickle.load(file)
    print(data_terbaca)
