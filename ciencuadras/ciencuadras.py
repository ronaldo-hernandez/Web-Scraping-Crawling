import requests
import json
import pandas as pd
from tqdm import tqdm

""" url = "https://api-backend.ciencuadras.com/prod/search-results/v1"

macro = pd.DataFrame()
for x in tqdm(range(0,360,20)):
    payload = {
        "radio": "2km",
        "size": 20,
        "transactionType": "venta",
        "department": "cundinamarca",
        "city": "soacha",
        "from": x
    }
    headers = {
        "authority": "api-backend.ciencuadras.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-419,es;q=0.9",
        "authorization": "Bearer eyJraWQiOiJSNDBGb0R1OFRKYVJjYUgzRlhQMzBhZXlvb09LSWgxS2tWUUxHMkZSQlJNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxdGNtbTczNDJqNjY2MW80NGdnYm80ajE2cCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiY2llbmN1YWRyYXMtcHJvZC1hcGktc2VydmVyXC9yZWFkIGNpZW5jdWFkcmFzLXByb2QtYXBpLXNlcnZlclwvd3JpdGUiLCJhdXRoX3RpbWUiOjE2NTkxMjgxNzUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1YyWGRBYmJtbiIsImV4cCI6MTY1OTEzMTc3NSwiaWF0IjoxNjU5MTI4MTc1LCJ2ZXJzaW9uIjoyLCJqdGkiOiIyY2Y5NjQyNC01NzExLTQxZjQtYTc4Ny01OTg1N2U0Yjk0OGMiLCJjbGllbnRfaWQiOiIxdGNtbTczNDJqNjY2MW80NGdnYm80ajE2cCJ9.D4VrzjdI8hwzD2JsrYKYGNRRVYpvNUrgcryVA0noQB_YUPLKQYpPnvI2obt9BBwgo9bPEZjT_WlzmIOeA2huQFZtTqBi3wWyUvZCUEp8daSFBYv0D0xY-YD8IYvg-bT4qLre56Tk5z8W-XwJ_blR4dsU_J_gNsTdbdxXstgkHqYcKm0PUN1TGSCOCbx6zUKZiQYICEnu-2BnVp6VNo4jtN5cGSFyPRfKDqlrBmFsOoikcBWEbkPx_Nap9Y4n57rtos2vnPkQ7ze8UgE4e6iW1SjPIOk-D9kRoiujedcFGNBI68O9MDF4tTARaF_05iy7_nLndabdhQ1pMlYIN5YAYg",
        "content-type": "application/json",
        "origin": "https://www.ciencuadras.com",
        "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '""macOS""',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['data']['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])


macro = pd.DataFrame()
import requests

url = "https://api-backend.ciencuadras.com/prod/search-results/v1"

payload = {
    "radio": "2km",
    "size": 20,
    "transactionType": "venta",
    "pathUrl": "/venta/choconta"
}
headers = {
    "authority": "api-backend.ciencuadras.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "authorization": "Bearer eyJraWQiOiJSNDBGb0R1OFRKYVJjYUgzRlhQMzBhZXlvb09LSWgxS2tWUUxHMkZSQlJNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxdGNtbTczNDJqNjY2MW80NGdnYm80ajE2cCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiY2llbmN1YWRyYXMtcHJvZC1hcGktc2VydmVyXC9yZWFkIGNpZW5jdWFkcmFzLXByb2QtYXBpLXNlcnZlclwvd3JpdGUiLCJhdXRoX3RpbWUiOjE2NTkxNTQ0NTIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1YyWGRBYmJtbiIsImV4cCI6MTY1OTE1ODA1MiwiaWF0IjoxNjU5MTU0NDUyLCJ2ZXJzaW9uIjoyLCJqdGkiOiI4ZjU0OGRhNi0xZjBiLTQ4MTktYmYyMC1hNWVlMzY3ZGY0OWQiLCJjbGllbnRfaWQiOiIxdGNtbTczNDJqNjY2MW80NGdnYm80ajE2cCJ9.ZYqyJk1GA-QnjVQ035tSeBWEym-MqJpFglC983IpFxOwl_2MeB79D7DH6SDwaCs7gpWrJHRtREpUU9YmXjWGvRzllwt2ZiP0AKOTDNkmVwYN7AJPYVSfEwivQobgvOcRvZLcskUEOImpl4Uwfie09sK4w26bIXf0wjISW0X8UAx82fqCmm5CwhVo4KDePQSBbMgZVGb6JQ-14hgt_HPfSnByhKf_aPB33ZBY0B2F_Bh4CyJAg4Zudi_gC3R8_jBYxdJPsUrxfXvZHx_yyBWufXDu7reQY2-2ytfpTIL6SkfPrkQvmtjDAdIk4sKuCJIFaT-atpjuMFTRYBdB1Gjeow",
    "content-type": "application/json",
    "origin": "https://www.ciencuadras.com",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
 """


url = "https://api-backend.ciencuadras.com/prod/search-results/v1"
macro = pd.DataFrame()
for x in tqdm(range(0,50,20)):
    payload = {
        "radio": "2km",
        "size": 20,
        "transactionType": "venta",
        "pathUrl": "/venta/quibdo",
        "from":x
    }
    headers = {
        "authority": "api-backend.ciencuadras.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-419,es;q=0.9",
        "authorization": "Bearer eyJraWQiOiJSNDBGb0R1OFRKYVJjYUgzRlhQMzBhZXlvb09LSWgxS2tWUUxHMkZSQlJNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxdGNtbTczNDJqNjY2MW80NGdnYm80ajE2cCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiY2llbmN1YWRyYXMtcHJvZC1hcGktc2VydmVyXC9yZWFkIGNpZW5jdWFkcmFzLXByb2QtYXBpLXNlcnZlclwvd3JpdGUiLCJhdXRoX3RpbWUiOjE2NjM5NTU1MDEsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1YyWGRBYmJtbiIsImV4cCI6MTY2Mzk1OTEwMSwiaWF0IjoxNjYzOTU1NTAxLCJ2ZXJzaW9uIjoyLCJqdGkiOiI1NGUwYWU3OC01ZmYyLTRhMWMtYTg0Yi1mY2UzNjhiMGM3YTQiLCJjbGllbnRfaWQiOiIxdGNtbTczNDJqNjY2MW80NGdnYm80ajE2cCJ9.jaT_kNenj0c_54fNFsVN8QjGOc9wCV7sf4eEdh3hepHSWfLJNsmcTRL-2kXD-Cz3R0a-PqEiYZTsnU81xNJ0zzzgMiNcKwmhCDGYGJ_qwhVK8gHq2rBf1UIQdW5-iT2XpPdWnFUOwi7ZKeaYuEUEMzw0HWfOxNfBHRV_9aNbRry1ualBSaeGD6sVIurqeprvKGYlYd8PnqNsbqj6LXUO0u8GvqrlMF2xQXRY9V8zj8kf0shj4_k8MR2YhT1ujz7MRtBhNZqHlhUlqY4epfAXUqI1h19ymBY7l61uqcZjNSyyyA9gUr-1Exf_ILAne8sc4QpgHaQt9Ms2aZsBT6u87g",
        "content-type": "application/json",
        "origin": "https://www.ciencuadras.com",
        "referer": "https://www.ciencuadras.com/",
        "sec-ch-ua": '""Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105""',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '""macOS""',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['data']['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

""" response = requests.request("POST", url, json=payload, headers=headers)
data_json = json.loads(response.text)
data_ = data_json['data']['results']
df = pd.DataFrame(data_)
macro = pd.concat([df,macro]) """

macro.to_csv('cien_cuadras_datos_2_20220923.csv', sep = ';', index = False)