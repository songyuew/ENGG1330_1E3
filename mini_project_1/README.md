# Foreign Exchange Rates Quote
This is a demo app used for ENGG1330 tutorial (working with dictionary and list).

## Instruction
Please download the project folder and open `starter.py`.
You do not need to work on `request.py`.

## Sample API Call Response

```
{
    "meta": {
        "LastUpdated": "2022-09-19T10:15:44+08:00",
        "TotalResults": 2,
        "Agreement": "Use of the APIs and any related data will be subject to terms and conditions."
    },
    "data": [
        {
            "Brand": [
                {
                    "BrandName": "HSBC",
                    "ExchangeRateType": [
                        {
                            "ExchangeRateTypeName": "Banknote",
                            "Notes": [
                                "The information shown is for indication only"
                            ],
                            "ExchangeRate": [
                                {
                                    "ExchangeRateTierBand": [
                                        {
                                            "CurrencyCode": "AUD",
                                            "CurrencyName": "Australian Dollar",
                                            "BankBuyRate": "5.19840",
                                            "BankSellRate": "5.33970",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "CAD",
                                            "CurrencyName": "Canadian Dollar",
                                            "BankBuyRate": "5.83170",
                                            "BankSellRate": "5.99600",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "EUR",
                                            "CurrencyName": "Euro",
                                            "BankBuyRate": "7.74480",
                                            "BankSellRate": "7.95840",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "JPY",
                                            "CurrencyName": "Japanese Yen",
                                            "BankBuyRate": "0.05401",
                                            "BankSellRate": "0.05563",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "NZD",
                                            "CurrencyName": "New Zealand Dollar",
                                            "BankBuyRate": "4.61900",
                                            "BankSellRate": "4.76200",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "GBP",
                                            "CurrencyName": "Pound Sterling",
                                            "BankBuyRate": "8.78800",
                                            "BankSellRate": "9.12200",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "CNY",
                                            "CurrencyName": "Renminbi",
                                            "BankBuyRate": "1.10440",
                                            "BankSellRate": "1.13290",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "SGD",
                                            "CurrencyName": "Singapore Dollar",
                                            "BankBuyRate": "5.49500",
                                            "BankSellRate": "5.65750",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "CHF",
                                            "CurrencyName": "Swiss Franc",
                                            "BankBuyRate": "8.01980",
                                            "BankSellRate": "8.23740",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "THB",
                                            "CurrencyName": "Thai Baht",
                                            "BankBuyRate": "0.19960",
                                            "BankSellRate": "0.22570",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        },
                                        {
                                            "CurrencyCode": "USD",
                                            "CurrencyName": "US Dollar",
                                            "BankBuyRate": "7.78570",
                                            "BankSellRate": "7.91250",
                                            "Notes": "The information shown is for indication only",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "ExchangeRateTypeName": "Telegraphic Transfer",
                            "Notes": [
                                "The information shown is for indication only"
                            ],
                            "ExchangeRate": [
                                {
                                    "ExchangeRateTierBand": [
                                        {
                                            "CurrencyCode": "AUD",
                                            "CurrencyName": "Australian Dollar",
                                            "BankBuyRate": "5.23010",
                                            "BankSellRate": "5.30780",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "CAD",
                                            "CurrencyName": "Canadian Dollar",
                                            "BankBuyRate": "5.86870",
                                            "BankSellRate": "5.95890",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "EUR",
                                            "CurrencyName": "Euro",
                                            "BankBuyRate": "7.78050",
                                            "BankSellRate": "7.92260",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "JPY",
                                            "CurrencyName": "Japanese Yen",
                                            "BankBuyRate": "0.05426",
                                            "BankSellRate": "0.05537",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "NZD",
                                            "CurrencyName": "New Zealand Dollar",
                                            "BankBuyRate": "4.64780",
                                            "BankSellRate": "4.73320",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "GBP",
                                            "CurrencyName": "Pound Sterling",
                                            "BankBuyRate": "8.87500",
                                            "BankSellRate": "9.03500",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "CNY",
                                            "CurrencyName": "Renminbi",
                                            "BankBuyRate": "1.11100",
                                            "BankSellRate": "1.12630",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "SGD",
                                            "CurrencyName": "Singapore Dollar",
                                            "BankBuyRate": "5.53240",
                                            "BankSellRate": "5.61960",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "CHF",
                                            "CurrencyName": "Swiss Franc",
                                            "BankBuyRate": "8.07050",
                                            "BankSellRate": "8.18660",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "THB",
                                            "CurrencyName": "Thai Baht",
                                            "BankBuyRate": "0.20820",
                                            "BankSellRate": "0.21700",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        },
                                        {
                                            "CurrencyCode": "USD",
                                            "CurrencyName": "US Dollar",
                                            "BankBuyRate": "7.81820",
                                            "BankSellRate": "7.88000",
                                            "LastUpdateDateTime": "2022-09-19T10:13:00+08:00",
                                            "Notes": "The information shown is for indication only"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```