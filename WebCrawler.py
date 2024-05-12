import requests
from bs4 import BeautifulSoup

URL = 'https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A0%D7%A1%D7%A0%D7%98_%D7%95%D7%90%D7%9F_%D7%92%D7%95%D7%9A'

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
r = requests.get(URL,headers)
#print(r.status_code)

soup = BeautifulSoup(r.content, features="html.parser")
#print(soup.prettify())
print('hello')

section = soup.find('a', attrs={'class':'mw-file-description'})
print(len(section))
print(section)