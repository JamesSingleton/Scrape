import requests
from bs4 import BeautifulSoup

response = requests.get("insert URL here")

soupBase = BeautifulSoup(response.content, 'html.parser')
#txt = response.text

g_data = soupBase.find("div", {"class": "mainWrapper"})
avail_prop = g_data.find_all("table", {"class":"availabilityTable"})
for property in avail_prop:
     beds = property.find('td', {'class': 'beds'}).find('span', {'class': 'longText'}).text
     baths = property.find('td', {'class': 'baths'}).find('span', {'class': 'longText'}).text
     rent = property.find('td', {'class': 'rent'}).text

     print('Bed:{} Bath:{} Rent:{}'.format(beds, baths, rent))

c_data = soupBase.find_all("div", {"class": "specList"})
for items in c_data:
    try:
        print (items.find_all("ul")[0].text)
    except:
        pass

#print(soupBase)
