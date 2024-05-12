import requests
from bs4 import BeautifulSoup
import bs4

head = 'https://'

URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
web = requests.get(URL)
print(web.status_code)
soup = BeautifulSoup(web.content)


def scrap_pics_from_wiki(soup):

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
    
        for x in range(len(tablet)):
            tale = tablet[x].partition('//')
            tale = tale[tale.index('//')+1]

            tablet[x] = head + tale
            tablet[x] = tablet[x].rstrip('"')
            print(tablet[x])

            img_name = str(i) + '_' + str(x) + '.jpg'
            img_data = requests.get(tablet[x]).content
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
            
    