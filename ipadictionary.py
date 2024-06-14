nilai_IPA = {'joni': 5,
             'edward': 8,
             'hendrik': 9,
             'siti': 6,
             'bagong': 7,
             'endang': 8,
             'bolot': 5,
             'edi': 7}

nama = input("masukkan nama siswa: ")

if nama in nilai_IPA:
    print("nilai IPA ", nama, " adalah ", nilai_IPA[nama])
else:
    print("data siswa tidak ditemukan.")
    print("berikut nama-nama siswa:")
    for i in nilai_IPA.keys():
        print(i)
