import requests
from bs4 import BeautifulSoup
import bs4

head = 'https://'

URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
web = requests.get(URL)
print(web.status_code)
soup = BeautifulSoup(web.content)

table = soup.find_all('img')

for i in range(len(table)): #need to heandle erorr cases
    section = table[i]

    txt = str(section)
    x = txt.find("src=")

    txt = txt.split()

    tablet = list()

    
    for x in range(len(txt)):    
        if txt[x].count('//upload') != 0:
            tablet.append(txt[x])       
    
       


    for i in range(len(tablet)):    
        tale = tablet[i].partition('//')[2]
        tablet[i] = head + tale
        tablet[i] = tablet[i].rstrip('"')
        print(tablet[i])

        img_name = str(i) + '.jpg'
        img_data = requests.get(tablet[i]).content
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
            
    