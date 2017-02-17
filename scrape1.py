import requests
from bs4 import BeautifulSoup
from config import *

#states = ['CA']

for state in states:
    state_url = base_url+"{}".format(state)+"/"
    print (state_url)
    ar = requests.get(state_url)
    soupBase = BeautifulSoup(ar.content, 'html.parser')
    pagination = soupBase.find_all("div", {"class": "paging"})
    for number in pagination:
        pages = number.find_all("a")[6]
        newPages = pages.get("data-page")
        intPages = int(newPages)
    #print (intPages)
    for i in range(intPages+1):
        try:
            target_url =state_url+"{}".format(i)
            r = requests.get(target_url)
            soupTarget = BeautifulSoup(r.content, 'html.parser')
            g_data = soupTarget.find_all("article", {"class": "placard"})
            community_url = []
            for item in g_data:
                try:
                    print (item.find_all("a", {"class": "placardTitle"})[0].text)
                    print (item.find_all("div", {"class": "location"})[0].text)
                    communityURL = item.find_all("a", {"class": "placardTitle"})[0].get('href')
                    community_url.append(communityURL)
                    print (communityURL, '\n')
                except:
                    pass
        except:
            pass
print (community_url)
print('done!')
