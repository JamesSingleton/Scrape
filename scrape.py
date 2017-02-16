import requests

response = requests.get("https://www.apartments.com/promenade-towers-los-angeles-ca/1ppnmg4/")

txt = response.text

print(txt)
