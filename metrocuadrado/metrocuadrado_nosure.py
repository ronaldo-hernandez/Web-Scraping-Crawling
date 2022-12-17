import requests
import pandas as pd
import json
from tqdm import tqdm
import json
import chompjs
from concurrent.futures import ThreadPoolExecutor
from requests_html import HTMLSession
import time
import pandas as pd
from csv import reader

macro = pd.DataFrame()

for x in tqdm(range(0,72)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"Chia","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,consultorio,edificio-de-oficinas,edificio-de-apartamentos","from":f"{x}","size":"50"}
    payload = ""
    headers = {
        "authority": "www.metrocuadrado.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-419,es;q=0.9",
        "cookie": "visid_incap_434661=vFMfPTjbRcmUtbjoLaCtlOxz22IAAAAAQUIPAAAAAACkEnUxsDUIpM0JQ+Ed3ylv; incap_ses_9219_434661=w3twUpCPfECvOETtIHjwf+xz22IAAAAALE6A482scKgHLEx2AnW5lw==; _gcl_au=1.1.1558921659.1658549230; _rtbhouse_source_=direct; _ga=GA1.2.307756145.1658549231; _gid=GA1.2.1066036661.1658549231; _fbp=fb.1.1658549230680.13669224; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_966913=eyJpZCI6IjJlZWNmZmI4LWEzZmMtNGViZC1hZWZhLTVjZjI1OGU5YTVhYSIsImNyZWF0ZWQiOjE2NTg1NDkyMzA4NjAsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; mzona=; mbarrio=; _gat_UA-42368290-2=1; _hjSessionUser_966913=eyJpZCI6Ijg2MGViYzgzLTc3MzMtNWMxYS1hNDU1LTQ1MDZjNWY2MmViNSIsImNyZWF0ZWQiOjE2NTg1NDkyMzA4MzcsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=89b48cface24eeec:T=1658549286:S=ALNI_MZSdS3VDjxPyUZJZdQpuVmLpksC4g; __gpi=UID=0000064de624399f:T=1658549286:RT=1658549286:S=ALNI_MbPgR7yJUCZh1RotPcVm_qXejSDog; disclaimerCookies=true; mciudad=; _dc_gtm_UA-42368290-2=1; mubicacion=cartagena-de-indias; location=Cartagena%20De%20Indias; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bconsultorio%3Bedificio-de-oficinas%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _conv_v=vi%3A1*sc%3A1*cs%3A1658549231*fs%3A1658549231*pv%3A4*exp%3A%7B%7D; _conv_s=si%3A1*sh%3A1658549230857-0.9398397572384112*pv%3A4; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-consultorio-edificio-de-oficinas-edificio-de-apartamentos%2Fventa%2Fusado%2Fcartagena-de-indias%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3DCartagena%20De%20Indias%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cconsultorio%2Cedificio-de-oficinas%2Cedificio-de-apartamentos",
        "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-consultorio-edificio-de-oficinas-edificio-de-apartamentos/venta/usado/chia/?search=form",
        "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '""macOS""',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
        "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,16)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"Fusagasuga","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,consultorio,edificio-de-oficinas,edificio-de-apartamentos","from":f"{x}","size":"50"}
    payload = ""
    headers = {
        "authority": "www.metrocuadrado.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-419,es;q=0.9",
        "cookie": "visid_incap_434661=vFMfPTjbRcmUtbjoLaCtlOxz22IAAAAAQUIPAAAAAACkEnUxsDUIpM0JQ+Ed3ylv; incap_ses_9219_434661=w3twUpCPfECvOETtIHjwf+xz22IAAAAALE6A482scKgHLEx2AnW5lw==; _gcl_au=1.1.1558921659.1658549230; _rtbhouse_source_=direct; _ga=GA1.2.307756145.1658549231; _gid=GA1.2.1066036661.1658549231; _fbp=fb.1.1658549230680.13669224; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_966913=eyJpZCI6IjJlZWNmZmI4LWEzZmMtNGViZC1hZWZhLTVjZjI1OGU5YTVhYSIsImNyZWF0ZWQiOjE2NTg1NDkyMzA4NjAsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; mzona=; mbarrio=; _gat_UA-42368290-2=1; _hjSessionUser_966913=eyJpZCI6Ijg2MGViYzgzLTc3MzMtNWMxYS1hNDU1LTQ1MDZjNWY2MmViNSIsImNyZWF0ZWQiOjE2NTg1NDkyMzA4MzcsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=89b48cface24eeec:T=1658549286:S=ALNI_MZSdS3VDjxPyUZJZdQpuVmLpksC4g; __gpi=UID=0000064de624399f:T=1658549286:RT=1658549286:S=ALNI_MbPgR7yJUCZh1RotPcVm_qXejSDog; disclaimerCookies=true; mciudad=; _dc_gtm_UA-42368290-2=1; mubicacion=cartagena-de-indias; location=Cartagena%20De%20Indias; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bconsultorio%3Bedificio-de-oficinas%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _conv_v=vi%3A1*sc%3A1*cs%3A1658549231*fs%3A1658549231*pv%3A4*exp%3A%7B%7D; _conv_s=si%3A1*sh%3A1658549230857-0.9398397572384112*pv%3A4; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-consultorio-edificio-de-oficinas-edificio-de-apartamentos%2Fventa%2Fusado%2Fcartagena-de-indias%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3DCartagena%20De%20Indias%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cconsultorio%2Cedificio-de-oficinas%2Cedificio-de-apartamentos",
        "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-consultorio-edificio-de-oficinas-edificio-de-apartamentos/venta/usado/fusagasuga/?search=form",
        "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '""macOS""',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
        "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,72)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"Chia","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,consultorio,edificio-de-oficinas,edificio-de-apartamentos","from":f"{x}","size":"50"}
    payload = ""
    headers = {
        "authority": "www.metrocuadrado.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-419,es;q=0.9",
        "cookie": "visid_incap_434661=vFMfPTjbRcmUtbjoLaCtlOxz22IAAAAAQUIPAAAAAACkEnUxsDUIpM0JQ+Ed3ylv; incap_ses_9219_434661=w3twUpCPfECvOETtIHjwf+xz22IAAAAALE6A482scKgHLEx2AnW5lw==; _gcl_au=1.1.1558921659.1658549230; _rtbhouse_source_=direct; _ga=GA1.2.307756145.1658549231; _gid=GA1.2.1066036661.1658549231; _fbp=fb.1.1658549230680.13669224; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_966913=eyJpZCI6IjJlZWNmZmI4LWEzZmMtNGViZC1hZWZhLTVjZjI1OGU5YTVhYSIsImNyZWF0ZWQiOjE2NTg1NDkyMzA4NjAsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; mzona=; mbarrio=; _gat_UA-42368290-2=1; _hjSessionUser_966913=eyJpZCI6Ijg2MGViYzgzLTc3MzMtNWMxYS1hNDU1LTQ1MDZjNWY2MmViNSIsImNyZWF0ZWQiOjE2NTg1NDkyMzA4MzcsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=89b48cface24eeec:T=1658549286:S=ALNI_MZSdS3VDjxPyUZJZdQpuVmLpksC4g; __gpi=UID=0000064de624399f:T=1658549286:RT=1658549286:S=ALNI_MbPgR7yJUCZh1RotPcVm_qXejSDog; disclaimerCookies=true; mciudad=; _dc_gtm_UA-42368290-2=1; mubicacion=cartagena-de-indias; location=Cartagena%20De%20Indias; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bconsultorio%3Bedificio-de-oficinas%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _conv_v=vi%3A1*sc%3A1*cs%3A1658549231*fs%3A1658549231*pv%3A4*exp%3A%7B%7D; _conv_s=si%3A1*sh%3A1658549230857-0.9398397572384112*pv%3A4; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-consultorio-edificio-de-oficinas-edificio-de-apartamentos%2Fventa%2Fusado%2Fcartagena-de-indias%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3DCartagena%20De%20Indias%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cconsultorio%2Cedificio-de-oficinas%2Cedificio-de-apartamentos",
        "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-consultorio-edificio-de-oficinas-edificio-de-apartamentos/venta/usado/chia/?search=form",
        "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '""macOS""',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
        "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

#macro.to_csv('metrocuadrado_20220722.csv', sep = ';', index = False)
macro = pd.read_csv('metrocuadrado_20220722.csv', sep = ';')
macro = macro.assign(value = 'https://www.metrocuadrado.com')
macro['link'] = macro['value']+''+macro['link']
links = macro['link'].tolist()

datos = []
def parse(url):
    s = HTMLSession()
    r = s.get(url,timeout = 20)
    info = 'script[type="application/json"]'
    script_txt = r.html.find(info, first = True).text.strip()
    json_data = chompjs.parse_js_object(script_txt)
    data = json.dumps(json_data)
    dt = json.loads(data)
    try:
        price = dt['props']['initialState']['realestate']['basic']['salePrice']
        rentprice = dt['props']['initialState']['realestate']['basic']['rentPrice']
        propertyId = dt['props']['initialState']['realestate']['basic']['propertyId']
        businessType = dt['props']['initialState']['realestate']['basic']['businessType']
        publicationStatus = dt['props']['initialState']['realestate']['basic']['publicationStatus']
        rentTotalPrice = dt['props']['initialState']['realestate']['basic']['rentTotalPrice']
        area = dt['props']['initialState']['realestate']['basic']['area']
        areac = dt['props']['initialState']['realestate']['basic']['areac']
        rooms = dt['props']['initialState']['realestate']['basic']['rooms']
        bathrooms = dt['props']['initialState']['realestate']['basic']['bathrooms']
        garages = dt['props']['initialState']['realestate']['basic']['garages']
        city = dt['props']['initialState']['realestate']['basic']['city']
        zone = dt['props']['initialState']['realestate']['basic']['zone']
        sector = dt['props']['initialState']['realestate']['basic']['sector']
        neighborhood = dt['props']['initialState']['realestate']['basic']['neighborhood']
        commonNeighborhood = dt['props']['initialState']['realestate']['basic']['commonNeighborhood']
        comment = dt['props']['initialState']['realestate']['basic']['comment']
        detail = dt['props']['initialState']['realestate']['basic']['detail']
        companyId = dt['props']['initialState']['realestate']['basic']['companyId']
        companyName = dt['props']['initialState']['realestate']['basic']['companyName']
        companyAddress = dt['props']['initialState']['realestate']['basic']['companyAddress']
        contactPhone = dt['props']['initialState']['realestate']['basic']['contactPhone']
        whatsapp = dt['props']['initialState']['realestate']['basic']['whatsapp']
        propertyState = dt['props']['initialState']['realestate']['basic']['propertyState']
        coord = dt['props']['initialState']['realestate']['basic']['coordinates']
        title = dt['props']['initialState']['realestate']['basic']['title']
        subtitle = dt['props']['initialState']['realestate']['basic']['subtitle']
        featured = dt['props']['initialState']['realestate']['basic']['featured']
        builtTime = dt['props']['initialState']['realestate']['basic']['builtTime']
        stratum = dt['props']['initialState']['realestate']['basic']['stratum']
        linkSeo = dt['props']['initialState']['realestate']['basic']['linkSeo']
        localPhone = dt['props']['initialState']['realestate']['basic']['localPhone']
        details = {
            'price':price,
            'rentprice':rentprice,
            'propertyId':propertyId,
            'businessType':businessType,
            'publicationStatus':publicationStatus,
            'publicationStatus':publicationStatus,
            'rentTotalPrice':rentTotalPrice,
            'rentTotalPrice':rentTotalPrice,
            'area':area,
            'areac':areac,
            'rooms':rooms,
            'bathrooms':bathrooms,
            'garages':garages,
            'city':city,
            'zone':zone,
            'sector':sector,
            'neighborhood':neighborhood,
            'commonNeighborhood':commonNeighborhood,
            'comment':comment,
            'detail':detail,
            'companyID':companyId,
            'companyName':companyName,
            'companyAddress':companyAddress,
            'contactPhone':contactPhone,
            'whatsapp':whatsapp,
            'propertyState':propertyState,
            'coordinates':coord,
            'title':title,
            'subtitle':subtitle,
            'featured':featured,
            'builtTime':builtTime,
            'stratum':stratum,
            'linkSeo':linkSeo,
            'localPhone':localPhone
            }
        datos.append(details)
        print(' Cantidad de datos extraidos :',len(datos))
    except:
        datos.append({})
        print('Fallido',len(details))
    return
### urls
### lenks
### lnks
#start = time.perf_counter()

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(parse,links) 

#fin = time.perf_counter() - start

#print('time take :', fin)

df = pd.DataFrame(datos)
print(df.head())
df['comment'] = df['comment'].str.replace('\n','')

df.to_csv('metro_cuadrado_data_bolivar_20220725.csv',index = False,sep = ";")



import requests



response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)


macro = pd.DataFrame()

for x in tqdm(range(0,1429,50)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","city":"Santa Marta","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":f"{x}","size":"50"}
    payload = ""
    headers = {
    "cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; incap_ses_989_434661=opVLWWWXTGDKMD3OEaO5DQwwT2MAAAAAedW5K4BNimbl6wupVwMAxA==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6ImY5ZTQ4ZDY1LTIxYTUtNGM4OC1iMDA1LWViNmFlNWU4YjAxYSIsImNyZWF0ZWQiOjE2NjYxMzQwMjkwNDQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjSession_966913=eyJpZCI6ImQxOGUwYzMyLWRkYjUtNDNhZS04ZTAwLTJjNGNkY2Y0YzU0NCIsImNyZWF0ZWQiOjE2NjYxMzQwNDA1MDMsImluU2FtcGxlIjpmYWxzZX0=; _dc_gtm_UA-42368290-2=1; _gat_UA-42368290-2=1; _ga=GA1.2.322710410.1663860182; _conv_v=vi%3A1*sc%3A3*cs%3A1666134033*fs%3A1663860183*pv%3A24*exp%3A%7B%7D*ps%3A1666129066; _conv_s=si%3A3*sh%3A1666134032524-0.26817649861547155*pv%3A4; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Fsantamarta%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Dsantamarta%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga_02LQXVPQF9=GS1.1.1666134028.2.1.1666134166.0.0.0; mubicacion=santa-marta; mciudad=Santa%20Marta; location=Santa%20Marta%20(Magdalena); mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:2$_se:13$_ss:0$_st:1666135967088$dc_visit:2$ses_id:1666134028418%3Bexp-session$_pn:5%3Bexp-session$dc_event:12%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/santa-marta/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])



macro = pd.DataFrame()
for x in tqdm(range(0,620,50)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"villavicencio","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":f"{x}","size":"50"}
    payload = ""
    headers = {
    "cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; disclaimerCookies=true; incap_ses_989_434661=GZzNVrYYbHbEoV3OEaO5DZZ5T2MAAAAAWztnuXawEBpQZn2r5c0I8Q==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6IjIyNzcyM2NkLTNmMGEtNGNiMi05YWFiLTUzZTdiNTZiNzY4NSIsImNyZWF0ZWQiOjE2NjYxNTI4NTUxMDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; mciudad=; mubicacion=villavicencio; location=villavicencio; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _gat_UA-42368290-2=1; _ga=GA1.2.322710410.1663860182; _dc_gtm_UA-42368290-2=1; _conv_v=vi%3A1*sc%3A4*cs%3A1666152855*fs%3A1663860183*pv%3A28*exp%3A%7B%7D*ps%3A1666134033; _conv_s=si%3A4*sh%3A1666152855305-0.21190604742531272*pv%3A2; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Fvillavicencio%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Dvillavicencio%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga_02LQXVPQF9=GS1.1.1666152854.4.1.1666152978.0.0.0; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:4$_se:7$_ss:0$_st:1666154778121$dc_visit:4$ses_id:1666152854145%3Bexp-session$_pn:3%3Bexp-session$dc_event:6%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/villavicencio/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

macro = pd.DataFrame()
for x in tqdm(range(0,117,50)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"florencia","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":f"{x}","size":"50"}
    payload = ""
    headers = {
    "cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; disclaimerCookies=true; incap_ses_989_434661=GZzNVrYYbHbEoV3OEaO5DZZ5T2MAAAAAWztnuXawEBpQZn2r5c0I8Q==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6IjIyNzcyM2NkLTNmMGEtNGNiMi05YWFiLTUzZTdiNTZiNzY4NSIsImNyZWF0ZWQiOjE2NjYxNTI4NTUxMDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; mciudad=; mubicacion=florencia; location=florencia; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _gat_UA-42368290-2=1; _dc_gtm_UA-42368290-2=1; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Fflorencia%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Dflorencia%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga=GA1.1.322710410.1663860182; _conv_v=vi%3A1*sc%3A4*cs%3A1666152855*fs%3A1663860183*pv%3A30*exp%3A%7B%7D*ps%3A1666134033; _conv_s=si%3A4*sh%3A1666152855305-0.21190604742531272*pv%3A4; _ga_02LQXVPQF9=GS1.1.1666152854.4.1.1666153950.0.0.0; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:4$_se:12$_ss:0$_st:1666155750460$dc_visit:4$ses_id:1666152854145%3Bexp-session$_pn:5%3Bexp-session$dc_event:11%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/florencia/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

macro = pd.DataFrame()
for x in tqdm(range(0,117,50)):
    url = "https://www.metrocuadrado.com/rest-search/search"
    querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"aguazul","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":"0","size":"50"}
    payload = ""
    headers = {"cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; disclaimerCookies=true; incap_ses_989_434661=GZzNVrYYbHbEoV3OEaO5DZZ5T2MAAAAAWztnuXawEBpQZn2r5c0I8Q==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6IjIyNzcyM2NkLTNmMGEtNGNiMi05YWFiLTUzZTdiNTZiNzY4NSIsImNyZWF0ZWQiOjE2NjYxNTI4NTUxMDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; mciudad=; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Fflorencia%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Dflorencia%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga=GA1.2.322710410.1663860182; _conv_v=vi%3A1*sc%3A4*cs%3A1666152855*fs%3A1663860183*pv%3A31*exp%3A%7B%7D*ps%3A1666134033; _conv_s=si%3A4*sh%3A1666152855305-0.21190604742531272*pv%3A5; _ga_02LQXVPQF9=GS1.1.1666152854.4.1.1666154226.0.0.0; mubicacion=aguazul; location=aguazul; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _gat_UA-42368290-2=1; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:4$_se:15$_ss:0$_st:1666156026970$dc_visit:4$ses_id:1666152854145%3Bexp-session$_pn:6%3Bexp-session$dc_event:14%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/aguazul/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data_json = json.loads(response.text)
    data_ = data_json['results']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])




url = "https://www.metrocuadrado.com/rest-search/search"
querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"aguazul","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":"0","size":"50"}
payload = ""
headers = {"cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; disclaimerCookies=true; incap_ses_989_434661=GZzNVrYYbHbEoV3OEaO5DZZ5T2MAAAAAWztnuXawEBpQZn2r5c0I8Q==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6IjIyNzcyM2NkLTNmMGEtNGNiMi05YWFiLTUzZTdiNTZiNzY4NSIsImNyZWF0ZWQiOjE2NjYxNTI4NTUxMDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; mciudad=; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Fflorencia%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Dflorencia%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga=GA1.2.322710410.1663860182; _conv_v=vi%3A1*sc%3A4*cs%3A1666152855*fs%3A1663860183*pv%3A31*exp%3A%7B%7D*ps%3A1666134033; _conv_s=si%3A4*sh%3A1666152855305-0.21190604742531272*pv%3A5; _ga_02LQXVPQF9=GS1.1.1666152854.4.1.1666154226.0.0.0; mubicacion=aguazul; location=aguazul; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _gat_UA-42368290-2=1; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:4$_se:15$_ss:0$_st:1666156026970$dc_visit:4$ses_id:1666152854145%3Bexp-session$_pn:6%3Bexp-session$dc_event:14%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/aguazul/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data_json = json.loads(response.text)
data_ = data_json['results']
df = pd.DataFrame(data_)
macro = pd.concat([df,macro])







url = "https://www.metrocuadrado.com/rest-search/search"
querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"riohacha","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":"0","size":"50"}
payload = ""
headers = {
    "cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; disclaimerCookies=true; incap_ses_989_434661=GZzNVrYYbHbEoV3OEaO5DZZ5T2MAAAAAWztnuXawEBpQZn2r5c0I8Q==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6IjIyNzcyM2NkLTNmMGEtNGNiMi05YWFiLTUzZTdiNTZiNzY4NSIsImNyZWF0ZWQiOjE2NjYxNTI4NTUxMDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; mciudad=; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Faguazul%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Daguazul%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga=GA1.2.322710410.1663860182; _conv_v=vi%3A1*sc%3A4*cs%3A1666152855*fs%3A1663860183*pv%3A32*exp%3A%7B%7D*ps%3A1666134033; _conv_s=si%3A4*sh%3A1666152855305-0.21190604742531272*pv%3A6; _hjSession_966913=eyJpZCI6Ijk1MThlOGM3LWU1NjEtNDE1MS05YjE0LTE5NjIzMGE4ZTFiNCIsImNyZWF0ZWQiOjE2NjYxNTQyMjc4NTUsImluU2FtcGxlIjpmYWxzZX0=; _ga_02LQXVPQF9=GS1.1.1666152854.4.1.1666154720.0.0.0; mubicacion=riohacha; location=riohacha; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _gat_UA-42368290-2=1; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:4$_se:18$_ss:0$_st:1666156521111$dc_visit:4$ses_id:1666152854145%3Bexp-session$_pn:7%3Bexp-session$dc_event:17%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/riohacha/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data_json = json.loads(response.text)
data_ = data_json['results']
df = pd.DataFrame(data_)
macro = pd.concat([df,macro])





url = "https://www.metrocuadrado.com/rest-search/search"
querystring = {"realEstateBusinessList":"venta","realEstateStatusList":"usado","locationsList":"vichada","realEstateTypeList":"apartamento,casa,oficina,local,bodega,lote,finca,edificio-de-oficinas,consultorio,edificio-de-apartamentos","from":"0","size":"50"}
payload = ""
headers = {"cookie": "visid_incap_434661=KwgFE/ERRR2kIXVyPZHCwNF9LGMAAAAAQUIPAAAAAACwlIySmAujbBoJKZ29yNnv; _gcl_au=1.1.729083532.1663860182; _fbp=fb.1.1663860182724.2086961218; _conv_r=s%3Awww.google.com*m%3Aorganic*t%3A*c%3A; mzona=; _hjSessionUser_966913=eyJpZCI6IjI1MWI1ZDMzLTJmN2UtNWFjZC04NTdkLTZlZjQ4YWIwYTFjMCIsImNyZWF0ZWQiOjE2NjM4NjAxODMwMDIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.468914012.1666129065; _hjSessionUser_3186637=eyJpZCI6ImY1NDU2NWJhLTM0NjktNTg4NC1hNTdiLWQxOGExMjE5NTQzNiIsImNyZWF0ZWQiOjE2NjYxMjkwNjU3MjUsImV4aXN0aW5nIjp0cnVlfQ==; _rtbhouse_source_=direct; mbarrio=; disclaimerCookies=true; incap_ses_989_434661=GZzNVrYYbHbEoV3OEaO5DZZ5T2MAAAAAWztnuXawEBpQZn2r5c0I8Q==; _hjIncludedInSessionSample=0; _hjSession_3186637=eyJpZCI6IjIyNzcyM2NkLTNmMGEtNGNiMi05YWFiLTUzZTdiNTZiNzY4NSIsImNyZWF0ZWQiOjE2NjYxNTI4NTUxMDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; mciudad=; _hjSession_966913=eyJpZCI6Ijk1MThlOGM3LWU1NjEtNDE1MS05YjE0LTE5NjIzMGE4ZTFiNCIsImNyZWF0ZWQiOjE2NjYxNTQyMjc4NTUsImluU2FtcGxlIjpmYWxzZX0=; lastSearch=%2Fapartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos%2Fventa%2Fusado%2Friohacha%2F%3Fsearch%3Dsave%26realEstateBusinessList%3Dventa%26realEstateStatusList%3Dusado%26locationsList%3Driohacha%26realEstateTypeList%3Dapartamento%2Ccasa%2Coficina%2Clocal%2Cbodega%2Clote%2Cfinca%2Cedificio-de-oficinas%2Cconsultorio%2Cedificio-de-apartamentos; _ga=GA1.2.322710410.1663860182; _conv_v=vi%3A1*sc%3A4*cs%3A1666152855*fs%3A1663860183*pv%3A33*exp%3A%7B%7D*ps%3A1666134033; _conv_s=si%3A4*sh%3A1666152855305-0.21190604742531272*pv%3A7; _ga_02LQXVPQF9=GS1.1.1666152854.4.1.1666154871.0.0.0; mubicacion=vichada; location=vichada; mtipoinmueble=apartamento%3Bcasa%3Boficina%3Blocal%3Bbodega%3Blote%3Bfinca%3Bedificio-de-oficinas%3Bconsultorio%3Bedificio-de-apartamentos; mtiponegocio=venta-usado; _gat_UA-42368290-2=1; utag_main=v_id:0183ed07f1c800026297a9e4891805075001e06d00dca$_sn:4$_se:21$_ss:0$_st:1666156671530$dc_visit:4$ses_id:1666152854145%3Bexp-session$_pn:8%3Bexp-session$dc_event:20%3Bexp-session$dc_region:us-east-1%3Bexp-session",
    "authority": "www.metrocuadrado.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-419,es;q=0.9",
    "referer": "https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/usado/vichada/?search=form",
    "sec-ch-ua": '""Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-api-key": "P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl",
    "x-requested-with": "XMLHttpRequest"}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data_json = json.loads(response.text)
data_ = data_json['results']
df = pd.DataFrame(data_)
macro = pd.concat([df,macro])




