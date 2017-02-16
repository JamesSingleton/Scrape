import requests
from bs4 import BeautifulSoup

base_url="your url here"
ar = requests.get(base_url)
soupBase = BeautifulSoup(ar.content, 'html.parser')
pagination = soupBase.find_all("div", {"class": "paging"})

for number in pagination:
    pages = number.find_all("a")[6]
    newPages = pages.get("data-page")
    intPages = int(newPages)
    #print (intPages)

for i in range(intPages+1):
    try:
        target_url =base_url+"{}".format(i)
        print (target_url)
        r = requests.get(target_url)
        soupTarget = BeautifulSoup(r.content, 'html.parser')
        g_data = soupTarget.find_all("article", {"class": "placard"})
        for item in g_data:
            #print (item.contents)
            try:
                print (item.find_all("a", {"class": "placardTitle"})[0].text)
                print (item.find_all("div", {"class": "location"})[0].text, '\n')
            except:
                pass
    except:
        pass

print('done!')
