from request import getRates

def getFX(currencyCode, allRates):
    """
    Your code here
    """
    rates = allRates["data"][0]["Brand"][0]["ExchangeRateType"][0]["ExchangeRate"][0]["ExchangeRateTierBand"]
    for currencyData in rates:
        if currencyData["CurrencyCode"] == currencyCode:
            print("Bank buy rate: " + currencyData["BankBuyRate"])
            print("Bank sell rate: " + currencyData["BankSellRate"])
            break

currencyCode = input("Please input your currency: ")
allRates = getRates()
getFX(currencyCode, allRates)