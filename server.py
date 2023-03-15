#from email import header
import requests
#from fake_useragent import UserAgent
import vars
import os
import json
base_url = f"{vars.serverURI}/kandle/server.php"
# base_url = f"{vars.serverURI}/Web/server.php"


def getLinks():
    try:

       
        response = requests.get(
            f'{base_url}?get-links=1')
        return response.json()
    except Exception as e:
        print('[SERVER => getLinks] Error: ', e)
        return []


def getChilds():
    try:
        #headers = UserAgent().random
        response = requests.get(
            f"{base_url}?get-childs=1")
          #response = requests.get(
           # f"{base_url}?get-childs=1", headers={'Content-type': headers})
        return response.json()
    except Exception as e:
        print('[SERVER => getChilds] Error: ', e)


def saveOnServer(id=False, final=''):
    query = f"?set-link=1&id={id}&url={final}"
   # headers = UserAgent().random
    response = requests.post(
        f'{base_url}{query}')
    return response.text


def replacer(str_):
    return str_.replace('\n', '').replace('\t', '').replace('\r', '')


def saveChildNames():
    names = []
    finalLinks = '.\\finalLinks.csv'
    try:
        with open(finalLinks, 'r', encoding='utf-8') as file:
            n = file.readlines()
            if len(n) > 0:
                for k in n:
                    k = k.split(',')
                    i = replacer(k[0])
                    y = replacer(k[1])
                    t = {'id': y, 'link': i}
                    names.append(t)
                
                r = requests.post(base_url, json={'names': 1, 'childs': names})
                print('successfully saved on server...')
                return r.text
            else:
                print('Not Saved Empty file finalLinks.csv')
        return False
    except Exception as e:
        print('[SERVER saveChildNames]', e)


if __name__ == '__main__':
    # print(getLinks())
    saveChildNames()
