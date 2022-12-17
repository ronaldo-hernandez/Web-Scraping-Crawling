import json
import requests
import pandas as pd
from tqdm import tqdm

url = "https://api.fincaraiz.com.co/document/api/1.0/listing/search"

macro = pd.DataFrame()
for x in tqdm(range(0,350,25)):
    payload = {
        "filter": {
            "offer": {"slug": ["sell"]},
            "locations": {"states": {"slug": ["colombia-bolívar"]}},
            "age": {"slug": ["MORE_THAN_30_YEARS"]}
        },
        "fields": {
            "exclude": [],
            "facets": [],
            "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
            "limit": 25,
            "offset": x,
            "ordering": [],
            "platform": 40,
            "with_algorithm": True
        }
    }
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(350,801,25)):
    payload = {
        "filter": {
            "offer": {"slug": ["sell"]},
            "locations": {"states": {"slug": ["colombia-bolívar"]}},
            "age": {"slug": ["MORE_THAN_30_YEARS"]}
        },
        "fields": {
            "exclude": [],
            "facets": [],
            "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
            "limit": 25,
            "offset": x,
            "ordering": [],
            "platform": 40,
            "with_algorithm": True
        }
    }
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])



for x in tqdm(range(0,350,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 10,
            "lte": 600000000
        },
        "age": {"slug": ["FROM_16_TO_30_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(350,825,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 10,
            "lte": 600000000
        },
        "age": {"slug": ["FROM_16_TO_30_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,350,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 600000000,
            "lte": 999999999
        },
        "age": {"slug": ["FROM_16_TO_30_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,350,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 1,
            "lte": 600000000
        },
        "age": {"slug": ["FROM_9_TO_15_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(350,700,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 1,
            "lte": 600000000
        },
        "age": {"slug": ["FROM_9_TO_15_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,350,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 600000000,
            "lte": 100000000000000030000000000000
        },
        "age": {"slug": ["FROM_9_TO_15_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(350,801,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 600000000,
            "lte": 100000000000000030000000000000
        },
        "age": {"slug": ["FROM_9_TO_15_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,626,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 1,
            "lte": 250000000
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,400,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 250000000,
            "lte": 550000000
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(400,801,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 250000000,
            "lte": 550000000
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,400,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 550000000,
            "lte": 875000000
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(400,950,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 550000000,
            "lte": 875000000
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(0,400,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 875000000,
            "lte": 99999999999999
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro = pd.concat([df,macro])

for x in tqdm(range(400,950,25)):
    payload = {
    "filter": {
        "offer": {"slug": ["sell"]},
        "locations": {"states": {"slug": ["colombia-bolívar"]}},
        "price": {
            "gte": 875000000,
            "lte": 99999999999999
        },
        "age": {"slug": ["FROM_1_TO_8_YEARS"]}
    },
    "fields": {
        "exclude": [],
        "facets": [],
        "include": ["area", "baths.id", "baths.name", "baths.slug", "client.client_type", "client.company_name", "client.first_name", "client.fr_client_id", "client.last_name", "client.logo.full_size", "garages.name", "is_new", "locations.cities.fr_place_id", "locations.cities.name", "locations.cities.slug", "locations.countries.fr_place_id", "locations.countries.name", "locations.countries.slug", "locations.groups.name", "locations.groups.slug", "locations.groups.subgroups.name", "locations.groups.subgroups.slug", "locations.neighbourhoods.fr_place_id", "locations.neighbourhoods.name", "locations.neighbourhoods.slug", "locations.states.fr_place_id", "locations.states.name", "locations.states.slug", "locations.location_point", "max_area", "max_price", "media.photos.list.image.full_size", "media.photos.list.is_main", "media.videos.list.is_main", "media.videos.list.video", "media.logo.full_size", "min_area", "min_price", "offer.name", "price", "products.configuration.tag_id", "products.configuration.tag_name", "products.label", "products.name", "products.slug", "property_id", "property_type.name", "fr_property_id", "fr_parent_property_id", "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"],
        "limit": 25,
        "offset": x,
        "ordering": [],
        "platform": 40,
        "with_algorithm": True}}
    headers = {
    "authority": "api.fincaraiz.com.co",
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.fincaraiz.com.co",
    "referer": "https://www.fincaraiz.com.co/",
    "sec-ch-ua": '"".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103""',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '""macOS""',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.request("POST", url, json=payload, headers=headers)
    data_json = json.loads(response.text)
    data_ = data_json['hits']['hits']
    df = pd.DataFrame(data_)
    macro.drop_duplicates().shape
    macro = pd.concat([df,macro])