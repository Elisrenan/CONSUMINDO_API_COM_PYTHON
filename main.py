import requests
#https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")


print (response)

bolsa_valores = response.json()

print(bolsa_valores)

bolsa_valores = dict(bolsa_valores)
for chave, valor in bolsa_valores["USDBRL"].items():
    print(f"{chave}: {valor}")
    print("\n")

