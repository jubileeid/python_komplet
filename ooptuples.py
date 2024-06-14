bands = [("Bayu", "vokalis", 5),
         ("Deri", "gitaris", 3),
         ("Joni", "gitaris",3),
         ("Yoyok","basist", 3),
         ("Edi", "drummer"),
         ("Beki", "keyboard", 2)]

honor = 45000000
sum_ranking = sum(ranking for nama, posisi, ranking in bands)

for nama, posisi, ranking in bands:
    share = ranking / sum_ranking * honor
    print(f"{nama}, pemain {posisi}, dapat honor {share} Rupiah.")