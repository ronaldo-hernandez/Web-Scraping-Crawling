from requests_html import HTMLSession,HTML
import chompjs
import pandas as pd
import json
import time
from csv import reader
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor as TPE
from selenium import webdriver
import numpy as np
#from seleniumwire import webdriver
#from seleniumwire.utils import decode
##------------------------:: Extracción de links ::------------------------------------------##

'imac : /Users/ronaldohernandez/Documents/chromedriver'
'macbook: /Users/Thony/Documents/chromedriver'
url = 'https://www.fincaraiz.com.co/inmueble'
driver = webdriver.Chrome(executable_path ='/Users/ronaldohernandez/Documents/chromedriver')
driver.get(url)
links = []
links.append('https://fincaraiz.com.co/finca-raiz/venta/choco?usado=true&pagina=1')
links.append('https://www.fincaraiz.com.co/finca-raiz/venta/la-guajira?pagina=1')
links.append('https://www.fincaraiz.com.co/finca-raiz/venta/la-guajira?pagina=2')

for x in range(0,39):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/quindio?pagina={x}&precioDesde=1&precioHasta=190000000')

for x in range(0,38):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/quindio?pagina={x}&precioDesde=190000000&precioHasta=350000000')

for x in range(0,40):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/quindio?pagina={x}&precioDesde=350000000&precioHasta=690000000')

for x in range(0,41):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/quindio?pagina={x}&precioDesde=690000000&precioHasta=1800000000')

for x in range(0,41):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/quindio?pagina={x}&precioDesde=1800000000&precioHasta=3000000000000000')

links.append('https://www.fincaraiz.com.co/finca-raiz/venta/amazonas?pagina=1')

""" for x in range(1,41):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=28&areaHasta=41&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=41&areaHasta=46&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=46&areaHasta=50&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=50&areaHasta=53&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=53&areaHasta=56&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=56&areaHasta=59&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=59&areaHasta=62&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=62&areaHasta=66&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=66&areaHasta=70&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=70&areaHasta=74&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=74&areaHasta=79&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=79&areaHasta=85&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=85&areaHasta=92&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=92&areaHasta=102&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=102&areaHasta=115&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=115&areaHasta=130&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=130&areaHasta=150&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=150&areaHasta=180&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=150&areaHasta=180&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=180&areaHasta=225&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=225&areaHasta=300&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=300&areaHasta=450&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=450&areaHasta=1500&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=1-8&areaDesde=1500&areaHasta=1000000&pagina={x}')
 """    
""" for x in range(1,41):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=28&areaHasta=41&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=41&areaHasta=46&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=46&areaHasta=50&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=50&areaHasta=53&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=53&areaHasta=56&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=56&areaHasta=59&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=59&areaHasta=62&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=62&areaHasta=66&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=66&areaHasta=70&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=70&areaHasta=74&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=74&areaHasta=79&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=79&areaHasta=85&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=85&areaHasta=92&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=92&areaHasta=102&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=102&areaHasta=115&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=115&areaHasta=130&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=130&areaHasta=150&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=150&areaHasta=180&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=150&areaHasta=180&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=180&areaHasta=225&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=225&areaHasta=300&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=300&areaHasta=450&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=450&areaHasta=1500&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=9-15&areaDesde=1500&areaHasta=1000000&pagina={x}')

for x in range(1,41):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=28&areaHasta=45&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=45&areaHasta=51&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=51&areaHasta=55&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=55&areaHasta=59&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=59&areaHasta=63&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=63&areaHasta=68&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=68&areaHasta=72&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=72&areaHasta=78&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=78&areaHasta=85&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=85&areaHasta=92&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=92&areaHasta=99&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=99&areaHasta=105&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=105&areaHasta=113&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=113&areaHasta=125&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=125&areaHasta=139&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=139&areaHasta=156&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=156&areaHasta=173&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=173&areaHasta=195&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=195&areaHasta=210&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=210&areaHasta=235&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=235&areaHasta=269&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=269&areaHasta=310&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=310&areaHasta=380&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=380&areaHasta=500&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=500&areaHasta=1800&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=16-30&areaDesde=1800&areaHasta=1000000&pagina={x}')

for x in range(1,41):
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=28&areaHasta=60&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=60&areaHasta=78&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=78&areaHasta=95&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=95&areaHasta=115&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=115&areaHasta=135&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=135&areaHasta=160&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=160&areaHasta=188&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=188&areaHasta=215&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=215&areaHasta=240&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=240&areaHasta=270&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=270&areaHasta=300&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=300&areaHasta=350&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=350&areaHasta=420&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=420&areaHasta=660&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=660&areaHasta=50000&pagina={x}')
    links.append(f'https://www.fincaraiz.com.co/finca-raiz/venta/cundinamarca?antiguedad=%3E30&areaDesde=660&areaHasta=1000000&pagina={x}') """
    

""" driver.get(links[0])
time.sleep(7)
for request in driver.requests:
    if request.response:
        if request.url.startswith('https://www.fincaraiz.com.co/_next/data/build/'):
            response = request.response
            body = decode(response.body, response.headers.get('Content-Encoding','identity'))
            decode_body = body.decode('utf-8')
            df_body = pd.json_normalize(json.loads(decode_body))
            df_ = pd.DataFrame(df_body['pageProps.features'][0]) """

""" dfd = pd.DataFrame(json.loads(decode_body))
pd.DataFrame((dfd['pageProps'].values)).T
pd.DataFrame(dfd) """

""" all_df = pd.DataFrame()
## 
for url in tqdm(links):
    driver.get(url)
    for request in driver.requests:
        if request.response:
            if request.url.startswith('https://www.fincaraiz.com.co/_next/data/build'):
                response = request.response
                body = decode(response.body, response.headers.get('Content-Encoding','identity'))
                decode_body = body.decode('utf-8')
                df_body = pd.json_normalize(json.loads(decode_body))
                df_ = pd.DataFrame(df_body['pageProps.features'][0])
    all_df = pd.concat([df_,all_df])
    time.sleep(3) """



'https://api.fincaraiz.com.co/document/api/1.0/listing/search'
'https://api.fincaraiz.com.co/document/api/1.0/listing/search'
#driver.find_element_by_css_selector('#PoliticaCookies > div > div > button').click()
#driver.find_element_by_css_selector('#olBCFilters > div:nth-child(1) > div > div > div.anchor').click()

#url1 = 'https://www.fincaraiz.com.co/finca-raiz/venta/huila?pagina=1'
#urlss = [url1,url2,url3,url4]

#len_pag = []
#for x in range(0,len(urlss)):
    #driver.get(urlss[x])
    #len_page = driver.find_element_by_css_selector(' nav > ul > li:nth-child(8) > button').text
    #len_pag.append(len_page)
    #print(len_page)

#for x in range(1,int(len_pag[3])):
'//*[@id="listingContainer"]/div[1]/article/a/@href'
urls = []
for x in tqdm(links):
    driver.get(x)
    tab = driver.find_elements_by_xpath('//*[@id="listingContainer"]/div/article/a')
    for p in tab:
        t = p.get_property('href')
        urls.append(t)
        #print("Numero de link extraido :",len(links))
    time.sleep(2)

urls = pd.unique(urls)
df = pd.DataFrame(urls)
df.to_csv('fincaraiz_links_20220923.csv',index = False)

### Extrac data from urls
""" urls = []
with open('fincaraiz_links_santamarta20220614.csv','r') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        urls.append(row[0])

urls = urls[1:14001] """


print('La cantidad urls a extraer',len(urls))
all_det = []
def parse(url):
    s = HTMLSession()
    r = s.get(url)
    ### inform for application/json
    info_css_2 = 'script[type="application/json"]'
    script_txt_2 = r.html.find(info_css_2,first = True).text.strip()
    json_data_2 = chompjs.parse_js_object(script_txt_2)
    ## data_2
    data_2= json.dumps(json_data_2)
    dta_2 = json.loads(data_2)
    ## datos
    try:
        fecha_publicacion = dta_2['props']['pageProps']['dates']['published']
    except:
        fecha_publicacion = np.nan
    try:
        description = dta_2['props']['pageProps']['description']
    except:
        description = np.nan
    try:
        estrato = dta_2['props']['pageProps']['stratum']['name']
    except:
        estrato = np.nan
    try:
        n_estrato = dta_2['props']['pageProps']['stratum']['id']
    except:
        n_estrato = np.nan
    try:
        price_M2 = dta_2['props']['pageProps']['priceM2']
    except:
        price_M2 = np.nan
    try:
        address = dta_2['props']['pageProps']['address']
    except:
        address = np.nan
    try:
        categories = dta_2['props']['pageProps']['categories']
    except:
        categories = np.nan
    try:
        contact = dta_2['props']['pageProps']['contact']
    except:
        contact = np.nan
    try:
        name = dta_2['props']['pageProps']['propertyType']['name']
    except:
        name = np.nan
    try:
        title = dta_2['props']['pageProps']['title']
    except:
        title = np.nan
    try:
        price = dta_2['props']['pageProps']['price']
    except:
        price = np.nan
    try:
        rooms = dta_2['props']['pageProps']['rooms']['id']
    except:
        rooms = np.nan
    try:    
        baths = dta_2['props']['pageProps']['baths']['id']
    except:
        baths = np.nan
    try:
        area_const = dta_2['props']['pageProps']['area']
    except:
        area_const = np.nan
    try:
        tipo_inmueble = dta_2['props']['pageProps']['client']['type']
    except:
        tipo_inmueble = np.nan
    try:
        first_name = dta_2['props']['pageProps']['client']['firstName']
    except:
        first_name = np.nan
    try:
        lastName = dta_2['props']['pageProps']['client']['lastName']
    except:
        lastName = np.nan
    try:
        lat = dta_2['props']['pageProps']['locations']['lat']
    except:
        lat = np.nan
    try:    
        lon = dta_2['props']['pageProps']['locations']['lng']
    except:
        lon = np.nan
    try:    
        pais = dta_2['props']['pageProps']['locations']['country']['name']
    except:
        pais = np.nan
    try:
        dept = dta_2['props']['pageProps']['locations']['state']['name']
    except:
        dept = np.nan
    try:
        ciudad = dta_2['props']['pageProps']['locations']['city']['name']
    except:
        ciudad = np.nan
    try:
        barrio = dta_2['props']['pageProps']['locations']['neighbourhood']['name']
    except:
        barrio = np.nan
    try:
        zona = dta_2['props']['pageProps']['locations']['zone']
    except:
        zona = np.nan
    try:
        condition = dta_2['props']['pageProps']['condition']
    except:
        condition = np.nan
    try:
        tiempo = dta_2['props']['pageProps']['age']['name']
    except:
        tiempo = np.nan
    try:
        garages = dta_2['props']['pageProps']['garages']['id']
    except:
        garages = np.nan
    try:
        floor = dta_2['props']['pageProps']['floor']['name']
    except:
        floor = np.nan
    try:
        parking = dta_2['props']['pageProps']['parking']
    except:
        parking = np.nan
    try:
        environment = dta_2['props']['pageProps']['environment']
    except:
        environment = np.nan
    url_page = url
    dett = {
            'fecha_publicacion':fecha_publicacion, 
            'description':description,
            'estrato':estrato, 
            'n_estrato':n_estrato, 
            'price_M2':price_M2,
            'address':address, 
            'categories':categories,
            'contact':contact,
            'name':name,
            'title':title,
            'price':price,
            'rooms':rooms,
            'baths':baths,
            'area_const':area_const,
            'tipo_inmueble':tipo_inmueble,
            'first_name':first_name,
            'lastName':lastName,
            'latitude':lat,
            'longitude':lon,
            'pais':pais,
            'dept':dept,
            'ciudad':ciudad,
            'barrio':barrio,
            'zona':zona,
            'condition':condition,
            'tiempo':tiempo,
            'garages':garages,
            'floor':floor,
            'parking':parking,
            'environment':environment,
            'url_page':url_page
        }
    all_det.append(dett)
    print("Amount of info :",len(all_det))


with TPE() as executor:
    executor.map(parse, urls)


df = pd.DataFrame(all_det)
print(df.shape)
df.to_csv('fincaraiz_datos_20220923.csv',index = False,sep = ';',encoding = 'utf-8')



