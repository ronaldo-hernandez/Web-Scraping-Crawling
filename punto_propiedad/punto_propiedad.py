from selenium import webdriver
import time
import pandas as pd
from csv import reader
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from requests_html import HTML
import numpy as np

### Se extraen los 4996 links en punto propiedad.
links = []
for x in range(2,110):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/soacha/list/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/soacha/list'
links.append(r)
 
for x in range(2,39):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/madrid/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/madrid'
links.append(r)

for x in range(2,79):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/cajica/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/cajica'
links.append(r)

for x in range(2,169):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/chia/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/chia'
links.append(r)

for x in range(2,36):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/cota/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/cota'

for x in range(2,137):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/zipaquira/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/zipaquira'
links.append(r)

for x in range(2,37):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/mosquera-cundinamarca/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/mosquera-cundinamarca'
links.append(r)

for x in range(2,29):
    urls = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/calera/p_{x}'
    links.append(urls)

r = f'https://www.puntopropiedad.com/venta/apartamentos,casas,villas-quintas/calera'
links.append(r)

urls_macro = []
for x in tqdm(links):
    s = HTMLSession()
    r = s.get(x)
    src = r.text
    html = HTML(html = src)
    testt = html.find("div.ad-data > div.data > h2 > a")
    for x in testt:
        urls_macro.append(x.absolute_links)


df = pd.DataFrame(urls_macro)
df[0] = df[0].str.replace('example.org','puntopropiedad.com')
df = df.drop_duplicates()
df.to_csv('punto_propiedad_links_cundinamarca_20220909.csv',index = False)
urls = df[0].tolist()

### importing the urls
urls = []
with open('punto_propiedad_links_cundinamarca_20220909.csv','r') as f:
    read_csv = reader(f)
    for row in read_csv:
        urls.append(row[0])

urls = pd.unique(urls)
urls =urls[1:len(urls)]
""" urls = urls[1:len(urls)] """


all_in = []
def parse(url):
    s = HTMLSession()
    r = s.get(url)
    try:    
        title = r.html.find('div#firstLine div h1',first = True).text
    except:
        title = np.nan
    try:
        subtitle = r.html.find('div#firstLine div h2',first = True).text
    except:
        subtitle = np.nan
    try:
        name_client = r.html.find('a.agency-listing-link div',first = True).text
    except:
        name_client = np.nan
    try:
        price = r.html.find('div.price h2',first = True).text
    except:
        price = np.nan
    try:
        detail_list = r.html.find('div.priceChars ul.details_list li')
        details_list = []
        for det in detail_list:
            details_list.append(det.text)
    except:
        details_list = np.nan
    try:
        address = r.html.find('span.location_info',first = True).text
    except:
        address = np.nan
    try:
        description = r.html.find('div.info p.description',first = True).text
    except:
        description = np.nan
    try:
        caract_int = r.html.find('div.dropdown-list.open.col-md4 ul.list li')
        carac_int_list = []
        for car_int in caract_int:
            carac_int_list.append(car_int.text)
    except:
        carac_int_list = np.nan
    try:
        caract_ext = r.html.find('div.dropdown-list.open.col-md6 ul.list li')
        carac_ext_list = []
        for car_ext in caract_ext:
            carac_ext_list.append(car_ext.text)
    except:
        carac_ext_list = np.nan
    try:
        caract_entorno = r.html.find('div.dropdown-list.open ul.list.col-md3 li')
        carac_ent_list = []
        for car_ent in caract_entorno:
            carac_ent_list.append(car_ent.text)
    except:
        carac_ent_list = np.nan
    try:
        location = r.html.find('div.dropdown-list.light.open.map-section div button',first = True).attrs
        lat = location['data-x']
    except:
        lat = np.nan
    try:
        location = r.html.find('div.dropdown-list.light.open.map-section div button',first = True).attrs
        lon = location['data-y']
    except:
        lon = np.nan
    detalles = {
            'titles':title,
            'subtitle':subtitle,
            'name_client':name_client,
            'price':price,
            'details_list':details_list,
            'address':address,
            'description':description,
            'caracteristicas_interiores':carac_int_list,
            'caracteristicas_exteriores':carac_ext_list,
            'caracteristicas_entorno':carac_ent_list,
            'latitude':lat,
            'longitude':lon,
            'url_page':url
    }
    all_in.append(detalles)
    print('link parsed:',len(all_in))
    return

#start = time.perf_counter()
#r = 0
#h = 20
#fin = time.perf_counter() - start
#print('Time taken:',fin)
rs = []
for r in range(0,9500,500):
    rs.append((r,r+500))

df_ = pd.DataFrame()
for r,h in tqdm(rs):
    with ThreadPoolExecutor() as executor:
        executor.map(parse,urls[r:h])
        
    df = pd.DataFrame(all_in)
    df['description'] = df['description'].str.replace('\n','')
    df_ = pd.concat([df,df_])

df_ = df_.drop_duplicates('url_page')
df_.to_csv(f'punto_propiedad_cundinamarca_data_20220909.csv',index = False,sep = ';', encoding='utf-8')