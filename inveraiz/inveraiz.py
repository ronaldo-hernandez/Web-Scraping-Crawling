from requests_html import HTML,HTMLSession
from tqdm import tqdm
import chompjs
import json
from bs4 import BeautifulSoup

urls = []
for x in range(0,29):
    urls.append(f'http://inveraiz.com/search?id_city=794&business_type%5B0%5D=for_sale&order_by=max_price&order=desc&page={x}&for_sale=1&for_rent=0&for_transfer=0&lax_business_type=1')

s = HTMLSession()
links = []
for n in tqdm(urls):
    r = s.get(n)
    lista = r.html.find('div.list-properties > div > div > div > figure > a')
    for x in lista:
        links.append(x.attrs['href'])

data_total = []
for i in tqdm(links):
    s = HTMLSession()
    r = s.get(i)
    script = 'script[type="application/ld+json"]'
    script_txt = r.html.find(script,first = True).text.strip()
    json_d = chompjs.parse_js_object(script_txt)
    data= json.dumps(json_d)
    dta = json.loads(data)
    titulo = dta['name']
    descripcion = dta['description']
    soup = BeautifulSoup(descripcion)
    descripcion = soup.get_text()
    descripcion = descripcion.replace('\xa0',' ').replace('\n','')
    direccion = dta['address'].strip('\n')
    latitud = dta['geo']['latitude']
    longitud = dta['geo']['longitude']
    cell_phone = dta['telephone']
    precio = r.html.find('div > div.col-md-10 > div > span',first = True).text.strip('$').replace('.','')
    detalles = r.html.find('div > div.col-md-9 > ul > li')
    detalles_ = []
    for x in detalles:
        detalles_.append(x.text.replace(':',"':'"))
    data_dict = {
        'titulo':titulo,'descripcion':descripcion,'direccion':direccion,'latitud':latitud,'longitud':longitud,'cell_phone':cell_phone,'precio':precio,
        'detalles':detalles_, 'url_page':i
    }
    data_total.append(data_dict)