# JSONVAT

This is a continuation of adamcooke/vat-rates, which was archived and is no longer maintained.
I do not intend to keep this project updated by doing my own research, but will depend on your PRs to keep the infomation up to date.

Instead of hosting the json on jsonvat.com, as Adam did before, this fork only contains JSON versions of all countries, and no ruby files.
The json files can be used directly from [here](https://raw.githubusercontent.com/paulluuk/vat-rates/master/vat_rates.json).

## Important Notes

This information is provided on an as-is basis. The authors or contributors cannot be held responsible for its accuracy or completeness. You use the data provided here entirely at your own risk.

## Updating VAT Rates

As I do not intend to keep VAT rates up to date myself, any pull requests with updated information will be gratefully received. To add a new VAT rate, simply add a `period` section to the appropriate file in the `rates_json` directory. For example:

```json
    {
      "rates": {
        "reduced": 5.0,
        "standard": 16.0
      },
      "effective_from": "2020-07-01"
    }
```

I will then manually run `combine_rates.py` as a two-step process to ensure quality.