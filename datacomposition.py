from bandcomposition import Bands
from bandcomposition import Anggota
import json 

class JSONDataLoader:
    def load_band(self):
        with open("data.json") as file:
            data = json.load(file)
        bands = [Bands(band["nama"], Anggota(band["posisi"], band["ranking"])) for band in data["band"]]        
        return bands

