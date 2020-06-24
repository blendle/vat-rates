import urllib.request, json


def get_latest_for_country(country_name, rate_name):
    with urllib.request.urlopen(
        "https://raw.githubusercontent.com/paulluuk/vat-rates/master/vat_rates.json"
    ) as url:
        data = json.loads(url.read().decode())

    # get the info for this specific country
    country = [rate for rate in data["rates"] if rate["name"] == country_name][0]

    # take the latest period for that country
    latest_period = max(country["periods"], key=lambda p: p.get("effective_from", ""))

    # get the specific rate that you're looking for, e.g. 'reduced' or 'standard'
    latest_rate = latest_period["rates"][rate_name]

    return latest_rate


if __name__ == "__main__":
    NL_reduced = get_latest_for_country("Netherlands", "reduced")
    print(NL_reduced)  # 9.0
    print(NL_reduced.__class__)  # float
