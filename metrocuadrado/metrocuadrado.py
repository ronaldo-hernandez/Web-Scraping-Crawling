import json
from threading import local
import chompjs
from concurrent.futures import ThreadPoolExecutor
from requests_html import HTMLSession
from selenium import webdriver
import time
import pandas as pd
from csv import reader
import numpy as np
driver = webdriver.Chrome(executable_path = '/Users/ronaldohernandez/Documents/chromedriver')
url_base = 'https://www.metrocuadrado.com'
driver.get(url_base)


""" driver.find_element_by_css_selector('#__next > div > div > div.Layout__LayoutStyled-sc-9y7jis-0.ibZBWk.page-container > section > div > div > div.disclamer-action.text-center.text-lg-left > a').click() """

""" precio_desde = driver.find_element_by_css_selector('#__next > div > div > div.Layout__LayoutStyled-sc-9y7jis-0.ibZBWk.page-container > div.Container-u38a83-0.jDuhNh.inner-container.container > div:nth-child(2) > div.Col-sc-14ninbu-0.lfGZKA.d-none.d-sm-block.col-md-4.col-lg-3 > div.sc-jqCOkK.ghoOCR.Panel-sc-1yxh53u-0.hRHiTs.has-filter.card > div > form > form > div:nth-child(1) > input')
precio_desde.send_keys('0')
precio_hasta = driver.find_element_by_css_selector('#__next > div > div > div.Layout__LayoutStyled-sc-9y7jis-0.ibZBWk.page-container > div.Container-u38a83-0.jDuhNh.inner-container.container > div:nth-child(2) > div.Col-sc-14ninbu-0.lfGZKA.d-none.d-sm-block.col-md-4.col-lg-3 > div.sc-jqCOkK.ghoOCR.Panel-sc-1yxh53u-0.hRHiTs.has-filter.card > div > form > form > div:nth-child(2) > input')
precio_hasta.send_keys('1000000000')
driver.find_element_by_css_selector('#filter-price').click()
 """

### extracción de datos
links = []
condition = True
while condition:
    block = driver.find_elements_by_css_selector('div.card-header a.sc-bdVaJa.ebNrSm')
    for e in block:
        i = e.get_attribute('href')
        links.append(i)
        print('Número de link extraido: ', len(links))
    try:
        driver.find_element_by_css_selector('.item-icon-next > a:nth-child(1)').click()
        time.sleep(3)
    except:
        condition = False

""" for x in range(1,102):
    driver.find_element_by_css_selector('.item-icon-next > a:nth-child(1)').click() """

## Se guardaron las dos partes
urls_df = pd.DataFrame(links)
urls_df.to_csv('links_mc_20220906.csv',index = False)

""" urls = []
for x in range(1,3):
    with open(f'links_mc_parte{x}_20220214.csv','r') as f:
        reader_csv = reader(f)
        for row in reader_csv:
            urls.append(row[0]) """

links = []
with open('links_mc_20220531.csv','r') as f:
    reader_csv = reader(f)
    for row in reader_csv:
        links.append(row[0])

links = pd.unique(links)
links = links[1:len(links)]

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
    except:
        price = np.nan
    try:
        rentprice = dt['props']['initialState']['realestate']['basic']['rentPrice']
    except:
        rentprice = np.nan
    try:
        propertyId = dt['props']['initialState']['realestate']['basic']['propertyId']
    except:
        propertyId = np.nan
    try:
        businessType = dt['props']['initialState']['realestate']['basic']['businessType']
    except:
        businessType = np.nan
    try:
        publicationStatus = dt['props']['initialState']['realestate']['basic']['publicationStatus']
    except:
        publicationStatus = np.nan
    try:
        rentTotalPrice = dt['props']['initialState']['realestate']['basic']['rentTotalPrice']
    except:
        rentTotalPrice = np.nan
    try:
        area = dt['props']['initialState']['realestate']['basic']['area']
    except:
        area = np.nan
    try:
        areac = dt['props']['initialState']['realestate']['basic']['areac']
    except:
        areac = np.nan
    try:
        rooms = dt['props']['initialState']['realestate']['basic']['rooms']
    except:
        rooms = np.nan
    try:
        bathrooms = dt['props']['initialState']['realestate']['basic']['bathrooms']
    except:
        bathrooms = np.nan
    try:
        garages = dt['props']['initialState']['realestate']['basic']['garages']
    except:
        garages = np.nan
    try:
        city = dt['props']['initialState']['realestate']['basic']['city']
    except:
        city = np.nan
    try:
        zone = dt['props']['initialState']['realestate']['basic']['zone']
    except:
        zone = np.nan
    try:
        sector = dt['props']['initialState']['realestate']['basic']['sector']
    except:
        sector = np.nan
    try:
        neighborhood = dt['props']['initialState']['realestate']['basic']['neighborhood']
    except:
        neighborhood = np.nan
    try:
        commonNeighborhood = dt['props']['initialState']['realestate']['basic']['commonNeighborhood']
    except:
        commonNeighborhood = np.nan
    try:
        comment = dt['props']['initialState']['realestate']['basic']['comment']
    except:
        comment = np.nan
    try:
        detail = dt['props']['initialState']['realestate']['basic']['detail']
    except:
        detail = np.nan
    try:
        companyId = dt['props']['initialState']['realestate']['basic']['companyId']
    except:
        companyId = np.nan
    try:
        companyName = dt['props']['initialState']['realestate']['basic']['companyName']
    except:
        companyName = np.nan
    try:
        companyAddress = dt['props']['initialState']['realestate']['basic']['companyAddress']
    except:
        companyAddress = np.nan
    try:
        contactPhone = dt['props']['initialState']['realestate']['basic']['contactPhone']
    except:
        contactPhone = np.nan
    try:
        whatsapp = dt['props']['initialState']['realestate']['basic']['whatsapp']
    except:
        whatsapp = np.nan
    try:
        propertyState = dt['props']['initialState']['realestate']['basic']['propertyState']
    except:
        propertyState = np.nan
    try:
        coord = dt['props']['initialState']['realestate']['basic']['coordinates']
    except:
        coord = np.nan
    try:
        title = dt['props']['initialState']['realestate']['basic']['title']
    except:
        title = np.nan
    try:
        subtitle = dt['props']['initialState']['realestate']['basic']['subtitle']
    except:
        subtitle = np.nan
    try:
        featured = dt['props']['initialState']['realestate']['basic']['featured']
    except:
        featured = np.nan
    try:
        builtTime = dt['props']['initialState']['realestate']['basic']['builtTime']
    except:
        builtTime = np.nan
    try:
        stratum = dt['props']['initialState']['realestate']['basic']['stratum']
    except:
        stratum = np.nan
    try:
        linkSeo = dt['props']['initialState']['realestate']['basic']['linkSeo']
    except:
        linkSeo = np.nan
    try:
        localPhone = dt['props']['initialState']['realestate']['basic']['localPhone']
    except:
        localPhone = np.nan
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
    'localPhone':localPhone}
    datos.append(details)
    print(' Cantidad de datos extraidos :',len(datos))
    return
### urls
### lenks
### lnks
start = time.perf_counter()

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(parse,links) 

fin = time.perf_counter() - start

print('time take :', fin)

df = pd.DataFrame(datos)
print(df.head())
df['comment'] = df['comment'].str.replace('\n','')

df.to_csv('metro_cuadrado_data_cundinamarca_20220906.csv',index = False,sep = ";")