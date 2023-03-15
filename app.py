from scrapper import Parasite
from server import getChilds, getLinks, saveOnServer
import time
# from vars import production
# import os
from renamer import Renamer
from vars import loading
count = 0
t = 0
if __name__ == '__main__':
    cache1 = Parasite(linktype='cache1')
    cache2 = Parasite(linktype='cache2')
    cache3 = Parasite(linktype='cache3')
    while True:
        if count >= 3:
            count = 0
        count += 1
        t += 1
        loading(before=f'Listening server [{t}]', scale=count)
        try:
            links = getLinks()
            for link in links:
                if link['cache'] == 'cache1':
                    cache1.CrackedMindBot(cache1.__filter__(
                        link['base_url']), open_only_browser=None)
                    print("EndResult:", cache1.end_url, "Id:", link['id'])
                    saveOnServer(
                        id=link["id"], final=cache1.end_url)
                    try:
                        if len(link["base_url"].split("id=")) > 0:
                            base_link_id = link["base_url"].split("id=")[1]
                        else:
                            base_link_id = link["base_url"]
                        print(
                            f'ID: {link["id"]} | file ID: {base_link_id}')
                    except:
                        print(
                            f'ID: {link["id"]} | file ID: {link["base_url"]}')
                elif link['cache'] == 'cache2':
                    cache2.CrackedMindBot(cache2.__filter__(
                        link['base_url']), open_only_browser=None)
                    print("EndResult:", cache2.end_url, "Id:", link['id'])
                    saveOnServer(
                        id=link["id"], final=cache2.end_url)
                    try:
                        if len(link["base_url"].split("id=")) > 0:
                            base_link_id = link["base_url"].split("id=")[1]
                        else:
                            base_link_id = link["base_url"]
                        print(
                            f'ID: {link["id"]} | file ID: {base_link_id}')
                    except:
                        print(
                            f'ID: {link["id"]} | file ID: {link["base_url"]}')
                elif link['cache'] == 'cache3':
                    cache3.CrackedMindBot(cache3.__filter__(
                        link['base_url']), open_only_browser=None)
                    print("EndResult:", cache3.end_url, "Id:", link['id'])
                    saveOnServer(
                        id=link["id"], final=cache3.end_url)
                    try:
                        if len(link["base_url"].split("id=")) > 0:
                            base_link_id = link["base_url"].split("id=")[1]
                        else:
                            base_link_id = link["base_url"]
                        print(
                            f'ID: {link["id"]} | file ID: {base_link_id}')
                    except:
                        print(
                            f'ID: {link["id"]} | file ID: {link["base_url"]}')
                else:
                    anonymouse_cache = Parasite(linktype='other')
                    anonymouse_cache.CrackedMindBot(anonymouse_cache.__filter__(
                        link['base_url']), open_only_browser=None)
                    print("EndResult:", anonymouse_cache.end_url,
                          "Id:", link['id'])
                    saveOnServer(
                        id=link["id"], final=anonymouse_cache.end_url)
                    try:
                        if len(link["base_url"].split("id=")) > 0:
                            base_link_id = link["base_url"].split("id=")[1]
                        else:
                            base_link_id = link["base_url"]
                        print(
                            f'ID: {link["id"]} | file ID: {base_link_id}')
                    except:
                        print(
                            f'ID: {link["id"]} | file ID: {link["base_url"]}')
                    scrap.destroy()
                    anonymouse_cache.destroy()

            childs = getChilds()
            if len(childs) > 0:
                print('Renaming links: ', len(childs))
                renamer = Renamer(childs)

        except Exception as e:
            print('_-_-_- ERROR:', e)
        time.sleep(3)
