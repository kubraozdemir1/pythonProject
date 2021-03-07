import requests
import json


api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency"
                           "/listings/latest?start=1&limit=10&convert=USD&"
                           "CMC_PRO_API_KEY=f1e4d2c9-ca98-4890-8b29-70ee91a81a86")

result = json.loads(api_request.content)

#print(result)

# total count
#print("Total count:", result["status"]["total_count"])

sepet = [
    {
        "sembol": "BTC",
        "miktar": 3,
        "fiyat": 48000
    },
    {
        "sembol": "ADA",
        "miktar": 300,
        "fiyat": 1.05
    },
    {
        "sembol": "LTC",
        "miktar": 48,
        "fiyat": 185
    }

]

print('----------------------')

portfoy_karzarar = 0

for i in range(10):
    for coin in sepet:
        if result["data"][i]["symbol"] == coin["sembol"]:
            coin_basina_karzarar = result["data"][i]["quote"]["USD"]["price"] - coin["fiyat"]
            toplam_maliyet = coin["miktar"] * coin["fiyat"]
            toplam_karzarar = coin_basina_karzarar * coin["miktar"]
            portfoy_karzarar = portfoy_karzarar + toplam_karzarar

            print(result["data"][i]["symbol"] + " - " + result["data"][i]["name"])
            print("Alış Fiyatı: ${0:.2f}".format(coin["fiyat"]))
            print("Güncel Fiyat: ${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]))
            print("Miktar:", coin["miktar"])
            print("Toplam Maliyet: ${0:.2f}".format(toplam_maliyet))
            print("Coin başına Kar/Zarar: ${0:.2f}".format(coin_basina_karzarar))
            print("Toplam Kar/Zarar: ${0:.2f}".format(toplam_karzarar))
            print('----------------------')
print('**************************')
print("Portföy Kar/Zarar: ${0:.2f}".format(portfoy_karzarar))
print('**************************')




