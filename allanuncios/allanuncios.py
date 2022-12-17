import numpy as np
from requests_html import HTMLSession
from tqdm import tqdm
import pandas as pd
urls = []
""" for n in range(2,8):
    urls.append(f'https://search.allanuncios.com.co/compra-casas-aptos/cundinamarca/t+{n}?lb=new&search=1&start_field=1&keywords=&cat_1=12&geosearch_text=Cundinamarca&searchGeoId=2&sp_common_price%5Bstart%5D=&sp_common_price%5Bend%5D=&sp_housing_nb_bedrs%5Bstart%5D=&sp_housing_nb_bedrs%5Bend%5D=&sp_common_main_type=')
 """
urls.append('https://search.allanuncios.com.co/inmuebles-finca-raiz/guajira?lb=new&search=1&start_field=1&keywords=&cat_1=3&geosearch_text=Guajira&searchGeoId=90&_gl=1%2A13lch45%2A_ga%2AMTYxMzA1Mjk2Ni4xNjU5NDQ4NDM4%2A_ga_ZFDBKNMGP5%2AMTY2MzkzODI3NC4xLjEuMTY2MzkzODI4MC4wLjAuMA..')
urls.append('https://search.allanuncios.com.co/inmuebles-finca-raiz/quindio?lb=new&search=1&start_field=1&keywords=&cat_1=3&geosearch_text=Quind%C3%ADo&searchGeoId=33&_gl=1%2A12d5hg2%2A_ga%2AMTYxMzA1Mjk2Ni4xNjU5NDQ4NDM4%2A_ga_ZFDBKNMGP5%2AMTY2MzkzODI3NC4xLjEuMTY2MzkzODI5Ny4wLjAuMA..')
""" urls.append('https://search.allanuncios.com.co/arrendar-cuarto/cundinamarca?lb=new&search=1&start_field=1&keywords=&cat_1=77&geosearch_text=Cundinamarca&searchGeoId=2&sp_housing_monthly_rent%5Bstart%5D=&sp_housing_monthly_rent%5Bend%5D=&sp_housing_nb_bedrs%5Bstart%5D=&sp_housing_nb_bedrs%5Bend%5D=') """

""" for n in range(2,4):
    urls.append(f'https://search.allanuncios.com.co/venta-terrenos/co/t+{n}?lb=new&search=1&start_field=1&keywords=&cat_1=123&geosearch_text=Cundinamarca&searchGeoId=2&sp_common_price%5Bstart%5D=&sp_common_price%5Bend%5D=&sp_housing_sq_ft%5Bstart%5D=&sp_housing_sq_ft%5Bend%5D=')
    urls.append(f'https://search.allanuncios.com.co/propiedades-comerciales/cundinamarca/t+{x}?lb=new&search=1&start_field=1&keywords=&cat_1=142&geosearch_text=Cundinamarca&searchGeoId=2')

for n in range(2,16):
    urls.append(f'https://search.allanuncios.com.co/inmuebles-finca-raiz/cundinamarca/t+{n}?lb=new&search=1&start_field=1&keywords=&cat_1=3&geosearch_text=Cundinamarca&searchGeoId=2')
 """
links = []
for x in tqdm(urls):
    s = HTMLSession()
    r = s.get(x)    
    block = r.html.find('div.clad__wrapper > div.clad__title > a')
    for x in block:
        links.append(x.attrs['href'])

links = pd.unique(links)

data = []
for x in tqdm(range(0,len(links))):
    r = s.get(links[x])
    try:
        titulo = r.html.search('"main_lang_title":"{}","')[0]
    except:
        titulo = np.nan
    try:
        latitud = r.html.search('"geo_latitude":"{}","')[0]
    except:
        latitud = np.nan
    try:
        longitud = r.html.search('"geo_longitude":"{}","')[0]
    except:
        longitud = np.nan
    try:
        tipo_inmueble = r.html.search('"subcat_code":"{}",')[0]
    except:
        tipo_inmueble = np.nan
    try:
        fecha_publicacion = r.html.search('"posted":"{}",')[0]
    except:
        fecha_publicacion = np.nan
    try:    
        precio = r.html.search('"sp_common_price":"{}",')[0]
    except:
        precio = np.nan
    try:
        descripcion = r.html.find('#kiwii-description-block > div > div > div.shortdescription.font-panel-content > p',first = True).text
    except:
        descripcion = np.nan
    try:
        elements = r.html.find('#details-tbl-specs',first = True).text.replace('\n',',')
    except:
        elements = np.nan
    dict_data = {
        'titulo':titulo,'latitud':latitud, 'longitud':longitud,'tipo_inmueble':tipo_inmueble, 'fecha_publicacion':fecha_publicacion,'precio':precio,
        'descripcion':descripcion,'elements':elements
    }
    data.append(dict_data)

df = pd.DataFrame(data)

df.to_csv('allanuncios_data_20220923.csv',index=False, sep = ';',encoding = 'utf-8')