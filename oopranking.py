bands = ["Bayu", 
        "Deri",
        "Joni",
        "Yoyok",
        "Edi",
        "Beki"]

honor = 45000000
ranking = 0

for band in bands:
    if band == "Bayu":
        ranking = ranking + 5
    elif band == "Deri":
        ranking = ranking + 3
    elif band == "Joni":
        ranking = ranking + 3
    elif band == "Yoyok":
        ranking = ranking + 3
    elif band == "Edi":
        ranking = ranking + 2
    elif band == "Beki":
        ranking = ranking + 2

for band in bands:
    share = 0
    if band == "Bayu":
        share = 5 / ranking * honor
    elif band == "Deri":
        share = 3 / ranking * honor
    elif band == "Joni":
        share = 3 / ranking * honor
    elif band == "Yoyok":
        share = 3 / ranking * honor
    elif band == "Edi":
        share = 2 /ranking * honor
    elif band == "Beki":
        share = 2 /ranking * honor
    print(f"{band} dapat {share} Rupiah.")
