class Bands:
    def __init__(self, nama, posisi, ranking):
        self.nama = nama
        self.posisi = posisi
        self.ranking = ranking

band = [
    Bands("Bayu", "vokalis", 5),
    Bands("Deri", "gitaris", 3),
    Bands("Joni", "gitaris", 3),
    Bands("Yoyok", "basist", 3),
    Bands("Edi", "drummer", 2)
    ]

honor = 45000000

# mendapatkan nilai total seluruh ranking
sum_ranking = sum(anggotaband.ranking for anggotaband in band)

for anggotaband in band:
    share = anggotaband.ranking / sum_ranking * honor
    print(f"{anggotaband.nama}, posisi {anggotaband.posisi}, dapat honor {share}")