import json
import os
import glob


def combine():

    files = glob.glob(os.path.join("rates_json", "*.json"))
    countries = []

    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
        countries += [data]

    d = {
        "details": "http://github.com/paulluuk/vat-rates",
        "version": 1,
        "rates": countries,
    }

    with open("vat_rates.json", "w+") as f:
        json.dump(d, f, indent=2)


if __name__ == "__main__":
    combine()
