class Bands:
    def __init__(self, nama):
        self.nama = nama

class Vokalis(Bands):
    posisi = "vokalis"
    ranking = 5

class Gitaris(Bands):
    posisi = "gitaris"
    ranking = 3

class Basist(Bands):
    posisi = "basist"
    ranking = 3

class Drummer(Bands):
    posisi = "drummer"
    ranking = 2

band = [Vokalis("Bayu"),
        Gitaris("Deri"),
        Gitaris("Joni"),
        Basist("Yoyok"),
        Drummer("Edi")
]

honor = 45000000

# mendapatkan nilai total seluruh ranking
sum_ranking = sum(anggotaband.ranking for anggotaband in band)

for anggotaband in band:
    share = anggotaband.ranking / sum_ranking * honor
    print(f"{anggotaband.nama}, posisi {anggotaband.posisi}, dapat honor {share}")
 
