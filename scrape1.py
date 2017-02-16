import requests
from bs4 import BeautifulSoup

target_url ="your url here"

r = requests.get(target_url)

soup = BeautifulSoup(r.content, 'html.parser')

# for link in soup.find_all('a'):
#     print(link.text,link.get('href'))

g_data = soup.find_all("article", {"class": "diamond"})

for item in g_data:
    #print (item.contents)
    print (item.find_all("a", {"class": "placardTitle"})[0].text)
    print (item.find_all("div", {"class": "location"})[0].text, '\n')
