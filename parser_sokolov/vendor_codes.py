from glob import glob
from tqdm import trange, tqdm
import json

vendor_codes = []
for i, item in enumerate(tqdm(glob("data/*.json"))):
    with open(item, "rb") as json_file:
        data = json.load(json_file)
        for unit in data:
            vendor_codes.append(unit)
with open("vendor_codes.csv", "w") as file:
    for unit in vendor_codes:
        file.write(unit)
        file.write("\n")
print(len(vendor_codes))
print(len(set(vendor_codes)))