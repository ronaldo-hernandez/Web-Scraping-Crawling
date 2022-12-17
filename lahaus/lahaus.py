from requests_html import HTML, HTMLSession
from tqdm import tqdm
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import numpy as np

urls = []
""" for x in range(1,21):
    urls.append(f'https://www.lahaus.com/venta/propiedades/soacha?pagina={x}') """
urls.append('https://www.lahaus.com/buscar?locations=armenia')

urls_macro = []
for x in tqdm(urls):
    s = HTMLSession()
    r = s.get(x)
    src = r.text
    html = HTML(html = src)
    links = html.find('div.card-info.flex.flex-col.flex-grow > h3 > a')
    for x in links:
        urls_macro.append(x.absolute_links)

urls_macro_d = pd.DataFrame(urls_macro)
urls_macro_d[0] = urls_macro_d[0].str.replace('example.org','lahaus.com')
urls_macro = urls_macro_d[0].to_list()
#urls_macro_d.to_csv('links_lahaus.csv',sep = ';',index = False)

from selenium import webdriver
driver = webdriver.Chrome(executable_path ='/Users/ronaldohernandez/Documents/chromedriver')

data = []
for x in tqdm(urls_macro):
    driver.get(x)
    latitud = driver.find_element_by_xpath('//*[@id="pdp-gallery-modal"]/div/div/div[3]/div[3]/div').get_attribute('latitude')
    longitud = driver.find_element_by_xpath('//*[@id="pdp-gallery-modal"]/div/div/div[3]/div[3]/div').get_attribute('longitude')
    data_dict = {
        'url_link': x, 'latitud':latitud, 'longitud':longitud
    }
    data.append(data_dict)

df_urls = pd.DataFrame(data)
#df_urls.to_csv('df_coordinates_lahaus.csv',sep = ';',index = False)

urls_macro = pd.read_csv('lahaus/links_lahaus.csv',sep = ';')
urls_macro = urls_macro.iloc[:,0].tolist()

data = []
def parse(url):
    s = HTMLSession()
    r = s.get(url)
    try:
        title = r.html.find('h1.font-semibold',first = True).text
    except:
        title = np.nan
    try:
        location = r.html.find('div.flex h2.font-regular.text-14',first = True).text
    except:
        location = np.nan
    try:
        props_labels = r.html.find('div.col-span-12 section.main-amenities-area div h3')
        props_values = r.html.find('div.col-span-12 section.main-amenities-area p')
        prop_lab_list = []
        for prop_lab in props_labels:
            prop_lab_list.append(prop_lab.text)
        prop_val_list = []
        for prop_val in props_values:
            prop_val_list.append(prop_val.text)
        props = dict(zip(prop_lab_list,prop_val_list))
    except:
        props = np.nan
    try:    
        caracts = r.html.find('div.show-more-component div.show-more-content div')
        caracts_list = []
        for cars in caracts:
            caracts_list.append(cars.text)
    except:
        caracts_list = np.nan
    try:
        zonas_com_list = []
        zonas_comunes = r.html.find('div.grid.grid-cols-2.text-lh-green-gray div')
        for zonas in zonas_comunes:
            zonas_com_list.append(zonas.text)
    except:
        zonas_com_list = np.nan
    try:
        precio = r.html.find('section.px-lh-24.pt-lh-24.pb-lh-8.bg-lh-extra-light-sky-blue.border-b.border-lh-light-sky-blue.rounded-t-lg.relative > p',first = True).text
    except:
        precio = np.nan
    try:    
        extras = r.html.find('div.grid.grid-cols-1 div.my-lh-12.flex.items-center')
        extras_labls = []
        for ex in extras:
            extras_labls.append(ex.text.split('\n'))
        extrass = extras_labls
    except:
        extrass = np.nan
    try:    
        more_values =  r.html.find('#anchor-hidden-costs > div > div')
        values_buttons = []
        for but in more_values:
            values_buttons.append(but.text.split('\n'))
    except:
        values_buttons = np.nan
    url_page = url
    detal = {
            'titulo':title,
            'ubicacion':location,
            'propiedades':props,
            'caracteristicas':caracts_list,
            'zonas_comunes':zonas_com_list,
            'precio':precio,
            'valores_extras':extrass,
            'more_values':values_buttons,
            'url_page':url_page}
    data.append(detal)
    print('Procesando',len(data))
    return

with ThreadPoolExecutor() as executor:
    executor.map(parse,urls_macro)

df_general = pd.DataFrame(data)

df_general.to_csv('lahaus_data_20220801.csv',sep = ';',index = False)