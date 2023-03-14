import requests# pip install
from datetime import datetime
import json

def currency_convert(currChoise, currNumb):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from={currChoise}&amount={currNumb}"

    payload = {}
    headers= {
      "apikey": "br1PF2A7Pml1bDHIWD5Ow8W4hh3XBFdt"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    resp = json.loads(response.text)

    return str(resp['result'])[0:6]



def currency_list():
    urlUSD = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=USD&amount=1"
    urlEUR = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=EUR&amount=1"
    urlTRY = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=TRY&amount=1"
    urlRUB = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=RUB&amount=1"
    urlKGS = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=KGS&amount=1"
    urlCNY = f"https://api.apilayer.com/exchangerates_data/convert?to=KZT&from=CNY&amount=1"

    payload = {}
    headers= {
      "apikey": "br1PF2A7Pml1bDHIWD5Ow8W4hh3XBFdt"
    }

    responseUSD = requests.request("GET", urlUSD, headers=headers, data = payload)
    responseEUR = requests.request("GET", urlEUR, headers=headers, data = payload)
    responseTRY = requests.request("GET", urlTRY, headers=headers, data = payload)
    responseRUB = requests.request("GET", urlRUB, headers=headers, data = payload)
    responseKGS = requests.request("GET", urlKGS, headers=headers, data = payload)
    responseCNY = requests.request("GET", urlCNY, headers=headers, data = payload)

    
    respUSD = json.loads(responseUSD.text)
    respEUR = json.loads(responseEUR.text)
    respTRY = json.loads(responseTRY.text)
    respRUB = json.loads(responseRUB.text)
    respKGS = json.loads(responseKGS.text)
    respCNY = json.loads(responseCNY.text)

    return f'USD - {str(respUSD["result"])[0:6]} kzt;\n\
EUR - {str(respEUR["result"])[0:6]} kzt;\n\
TRY - {str(respTRY["result"])[0:6]} kzt;\n\
RUB - {str(respRUB["result"])[0:6]} kzt;\n\
KGS - {str(respKGS["result"])[0:6]} kzt;\n\
CNY - {str(respCNY["result"])[0:6]} kzt;'
                        



