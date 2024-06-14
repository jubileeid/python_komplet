from band import Vokalis
from band import Gitaris
from band import Basist
from band import Drummer
import json 

class DataLoader:
    def load_band(self):
        return [
            Vokalis("Bayu"),
            Gitaris("Deri"),
            Gitaris("Joni"),
            Basist("Yoyok"),
            Drummer("Edi")
        ]

class JSONDataLoader:
    def load_band(self):
        with open("data.json") as file:
            data = json.load(file)
        bands = []
        for band in data["band"]:
            if band["posisi"] == "vokalis":
                bands.append(Vokalis(band["nama"]))
            elif band["posisi"] == "gitaris":
                bands.append(Gitaris(band["nama"]))
            elif band["posisi"] == "basist":
                bands.append(Basist(band["nama"]))
            elif band["posisi"] == "drummer":
                bands.append(Drummer(band["nama"]))
        return bands