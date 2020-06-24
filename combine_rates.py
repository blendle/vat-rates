import json
import os
import glob


def combine():

    files = glob.glob(os.path.join("rates_json", "*.json"))
    countries = []

    for file in files:
        with open(file, "r") as f:
            data = json.load(f)

        # if no date provided, add a dummy date
        for block in data["periods"]:
            if not block.get("effective_from", None):
                block["effective_from"] = "0001-01-01"
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
