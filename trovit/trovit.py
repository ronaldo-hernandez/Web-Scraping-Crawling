from requests_html import HTML,HTMLSession
from tqdm import tqdm
import numpy as np
import pandas as pd
from csv import reader


links = []
for x in range(1,75):
    links.append(f'https://casas.trovit.com.co/index.php/cod.search_homes/type.1/what_d.soacha/rooms_min.0/bathrooms_min.0/resultsPerPage.25/isUserSearch.1/page.{x}')


urls_macro = []
for x in tqdm(links):
    s = HTMLSession()
    r = s.get(x)
    src = r.text
    html = HTML(html = src)
    testt = html.find("div > div > div.snippet-content > a")
    for i in testt:
        urls_macro.append(i.absolute_links)

urls = pd.DataFrame(urls_macro)
#urls.to_csv('urls_trovit_cundinamarca.csv',sep = ';',index=False)

urls = []
with open('/Users/ronaldohernandez/Library/Mobile Documents/com~apple~CloudDocs/Documents/Data_Analyst_DANE/DATA_ANALYST_2022/JUNIO_&_JULIO_2022/WEEK_4/Web_Scrapping_Cundinamarca/trovit/urls_trovit_cundinamarca.csv','r') as f:
    read_csv = reader(f)
    for row in read_csv:
        urls.append(row[0])

urls_macro = urls[1:len(urls)]


data = []
for x in tqdm(urls_macro):
    s = HTMLSession()
    r = s.get(x)
    try:
        titulo = r.html.find('#main_info > h1',first = True).text
    except:
        titulo = np.nan
    try:
        ubicacion = r.html.find('#main_info > h2',first = True).text
    except:
        ubicacion = np.nan
    try:
        properties = r.html.find('#main_info > div.properties > div')
        proper = []
        for x in properties:
            proper.append(x.text)
    except:
        proper = np.nan
    try:
        precio = r.html.find('#main_info > div.price > div > div.amount',first = True).text.strip('$')
    except:
        precio = np.nan
    try:
        administracion = r.html.find('#main_info > div.price > div > div.community_fee',first = True).text
    except:
        administracion = np.nan
    try:
        descripcion = r.html.find('#description',first = True).text.replace('\n',' ').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n').lower()
    except:
        descripcion = np.nan
    try:
        amenities = r.html.find('#amenities > ul > li > div.amenity-key')
        t_amenities = []
        for x in amenities:
            t_amenities.append(x.text)
        amenities = r.html.find('#amenities > ul > li > div.amenity-value')
        v_amenities = []
        for x in amenities:
            v_amenities.append(x.text)
        amenities = dict(zip(t_amenities,v_amenities))
    except:
        amenities = np.nan
    try:
        longitud = r.html.find('#map',first = True).attrs['data-longitude']
    except:
        longitud = np.nan
    try:
        latitud = r.html.find('#map',first = True).attrs['data-latitude']
    except:
        latitud = np.nan
    diccionario = {
        'titulo':titulo, 'ubicacion':ubicacion, 'properties':proper, 'precio':precio, 'administracion':administracion, 'descripcion':descripcion, 'amenities':amenities, 'longitud':longitud,
        'latitud':latitud}
    data.append(diccionario)

df = pd.DataFrame(data)
df.to_csv('data_trovit_cundinamarca.csv',sep = ';',index=False)



from requests_html import HTML,HTMLSession
from tqdm import tqdm
import numpy as np
import pandas as pd
from csv import reader


links = []
for x in range(1,101):
    links.append(f'https://casas.trovit.com.co/index.php/cod.search_homes/type.1/what_d.santa%20marta/rooms_min.0/bathrooms_min.0/resultsPerPage.25/isUserSearch.1/page.{x}')


urls_macro = []
for x in tqdm(links[0:10]):
    s = HTMLSession()
    r = s.get(x)
    src = r.text
    html = HTML(html = src)
    testt = html.find("div > div > div.snippet-content > a")
    for i in testt:
        urls_macro.append(i.absolute_links)

output_table = pd.DataFrame(urls_macro)

