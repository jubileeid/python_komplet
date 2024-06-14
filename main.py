
from data import DataLoader
from data import JSONDataLoader

# loader = DataLoader()
loader = JSONDataLoader()
band = loader.load_band()

honor = 45000000

# mendapatkan nilai total seluruh ranking
sum_ranking = sum(anggotaband.ranking for anggotaband in band)

for anggotaband in band:
    share = anggotaband.ranking / sum_ranking * honor
    print(f"{anggotaband.nama}, posisi {anggotaband.posisi}, dapat honor {share}")