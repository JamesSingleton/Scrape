import requests

response = requests.get("your url here")

txt = response.text

print(txt)
