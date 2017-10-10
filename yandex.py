import requests
from time import gmtime, strftime
import codecs

#r=requests.get("https://cloud-api.yandex.net/v1/disk/", headers={"Authorization":"OAuth AQAAAAABxUrPAASU7iFXBoODIk86ijcygra1E-I"});

def print_file(d):
    path = d['path'].replace('disk:/_ВИДЕОАРХИВ/', '').replace('disk:/_ФОТОАРХИВ/', '')
    path = path.replace("/", "\\")
    size = round(d['size'] / 1024, 2)
    text = "{0}, {1}".format(path, size)
    FLOG.write(text + "\n")

def load_data(path):
    print("Загружаю папку: {0}".format(path))
    r=requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=" + path + "&sort=name&limit=99999&fields=_embedded.items.type,_embedded.items.path,_embedded.items.size", headers={"Authorization":"OAuth AQAAAAABxUrPAASU7iFXBoODIk86ijcygra1E-I"});
    a = r.json();
    data = a['_embedded']['items']
    for d in data:
        if (d['type'] == 'dir'):
            load_data(d['path'])
        elif (d['type'] == 'file'):
            print_file(d)

def load(path):
    r=requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=" + path, headers={"Authorization":"OAuth AQAAAAABxUrPAASU7iFXBoODIk86ijcygra1E-I"});
    a = r.json();
    data = a['_embedded']['items']
    for d in data:
        if (d['name'] == '_ВИДЕОАРХИВ') or (d['name'] == '_ФОТОАРХИВ'):
            FLOG.write("\n" + d['name'] + "\n\n")
            load_data(d['path'])

FLOG = codecs.open('log_{0}.log'.format(strftime("%Y%m%d_%H%M%S", gmtime())), 'w', "utf-8")
   
load("/")
