import requests, config
from bs4 import BeautifulSoup
from pprint import pprint

#looping through each state page
for state in config.states:
    state_url = "{}{}/".format(config.base_url, state)
    print (state_url)
    ar = requests.get(state_url)
    soupBase = BeautifulSoup(ar.content, 'html.parser')
    pagination = soupBase.find_all("div", {"class": "paging"})
    for number in pagination:
        pages = number.find_all("a")[6]
        newPages = pages.get('data-page',0)
        intPages = int(newPages)
    #Grabbing the information per page within that state page
    community_url = [] #Setting community url array
    for i in range(intPages+1):
        try:
            target_url = "{}{}".format(state_url, i)
            r = requests.get(target_url)
            soupTarget = BeautifulSoup(r.content, 'html.parser')
            g_data = soupTarget.find_all("article", {"class": "placard"})

            #looping through each item on the page to grab name and location
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
pprint(community_url)
print('done!')
