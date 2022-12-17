import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from requests_html import HTMLSession
import time
from csv import reader
import chompjs
import json
import numpy as np

#### extracción de links:

links = []
for x in range(1,146):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:0-125000000?page={x}')

for x in range(1,141):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:125000000-150000000?page={x}')

for x in range(1,162):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:150000000-185000000?page={x}')

for x in range(1,144):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:185000000-230000000?page={x}')

for x in range(1,157):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:230000000-275000000?page={x}')

for x in range(1,165):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:275000000-320000000?page={x}')

for x in range(1,184):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:320000000-360000000?page={x}')

for x in range(1,233):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:360000000-420000000?page={x}')

for x in range(1,178):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:420000000-475000000?page={x}')

for x in range(1,178):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:475000000-550000000?page={x}')

for x in range(1,212):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:550000000-640000000?page={x}')

for x in range(1,206):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:640000000-750000000?page={x}')

for x in range(1,226):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:750000000-900000000?page={x}')

for x in range(1,334):
    links.append(f'https://www.properati.com.co/s/cundinamarca-colombia/venta/precio:2100000000-40000000000?page={x}')

l_links = []
def request(url):
    s = HTMLSession()
    r = s.get(url)
    block = r.html.find('div.StyledCard-sc-6ce7as-1.gxrAFy > div > a')
    baseurl = 'https://www.properati.com.co'
    link_ = [baseurl + link.attrs['href'] for link in block]
    l_links.extend(list(dict.fromkeys(link_)))
    print('Cantidad de links extraídos:',len(l_links))

with ThreadPoolExecutor() as executor:
    executor.map(request,links)

l_links_1 = pd.unique(l_links)
df = pd.DataFrame(l_links_1)
df.to_csv('properati_links_cundinamarca_20220907.csv',index = False)
###### extrac data
""" links = []
with open('properati_links_bolivar_20220726.csv','r') as f:
    reader_csv = reader(f)
    for row in reader_csv:
        links.append(row[0])

links = links[1:len(links)] """
links = l_links_1 

all_details = []
def parse(url):
    ### Extract data from url
    s = HTMLSession()
    r = s.get(url)
    ### inform for application/json
    info_css_2 = 'script[type="application/json"]'
    script_txt_2 = r.html.find(info_css_2,first = True).text.strip()
    json_data_2 = chompjs.parse_js_object(script_txt_2)
    ## data_2
    data_2= json.dumps(json_data_2)
    dta_2 = json.loads(data_2)
    ## Information details
    try:
        url_page = dta_2['props']['pageProps']['canonicalUrl']
    except:
        url_page = np.nan
    try:
        internal_id = dta_2['props']['pageProps']['property']['internal_id']
    except:
        internal_id = np.nan
    try:
        title = dta_2['props']['pageProps']['property']['title']
    except:
        title = np.nan
    try:
        description= dta_2['props']['pageProps']['property']['description']
    except:
        description= np.nan
    try:
        type_registro= dta_2['props']['pageProps']['property']['type']
    except:
        type_registro = np.nan
    try:    
        estr= dta_2['props']['pageProps']['property']['stratum']
    except:
        estr = np.nan
    try:
        direccion= dta_2['props']['pageProps']['property']['address']
    except:
        direccion = np.nan
    try:    
        precio= dta_2['props']['pageProps']['property']['price']['amount']
    except:
        precio = np.nan
    try:
        features = dta_2['props']['pageProps']['property']['features']
    except:
        features = np.nan
    try:
        floor_plant = dta_2['props']['pageProps']['property']['floor_plan']
    except:
        floor_plant = np.nan
    try:
        geo_location = dta_2['props']['pageProps']['property']['place']['parent_names']
    except:
        geo_location = np.nan
        ## coordinates
    try:
        lat = dta_2['props']['pageProps']['property']['geo_point']['lat']
    except:
        lat = np.nan
    try:
        lon = dta_2['props']['pageProps']['property']['geo_point']['lon']
    except:    
        lon = np.nan
    try:
        tag = dta_2['props']['pageProps']['property']['tags']
    except:
        tag = np.nan
    try:
        published_on = dta_2['props']['pageProps']['property']['published_on']
    except:
        published_on = np.nan
    try:
        created_on = dta_2['props']['pageProps']['property']['created_on']
    except:
        created_on = np.nan
    try:
        place = dta_2['props']['pageProps']['property']['place']
    except:
        place = np.nan
    try:
        seller = dta_2['props']['pageProps']['property']['seller']
    except:
        seller = np.nan
    try:
        agent = dta_2['props']['pageProps']['property']['agent']
    except:
        agent = np.nan
    det = {
        'id':internal_id,
        'url_page':url_page,
        'titulo':title,
        'description': description,
        'tipo': type_registro,
        'estrato': estr,
        'direccion':direccion,
        'precio':precio,
        'features':features,
        'floor_plant':floor_plant,
        'lat':lat,
        'lon':lon,
        'published_on':published_on,
        'place':place,
        'seller':seller,
        'agent':agent,
        'tag':tag,
        'create_on':created_on,
        'geo_location':geo_location
        }
    print("La cantidad de registros son:",len(all_details))
    all_details.append(det)
    return

with ThreadPoolExecutor() as executor:
    executor.map(parse,links)

df_1 = pd.DataFrame(all_details)
df_1['description'] = df_1['description'].replace('<br/>',' ')

df_1.to_csv('properati_cundinamarca_20220907.csv',index = False)