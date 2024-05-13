import requests
from bs4 import BeautifulSoup
import bs4


def links_scraper(web):#need to change to liks
    
    head = 'https://he.wikipedia.org/w'

    soup = BeautifulSoup(web.text, 'html.parser')

    table = soup.find_all('p')

    links = list()

    for i in range(len(table)): 
      
        txt = str(table[i])       
        txt = txt.split()

        tablet = list()                                 #creat a list
    
    
        for x in range(len(txt)):
            if txt[x].count("href=") != 0:              #Puts in the links (dirty)
                tablet.append(txt[x])       
    
     
          
        for x in range(len(tablet)):                    #cleaning the link
            
            tale = tablet[x].partition('/w')
            
            if tale.count('/w') != 0:
                tale = tale[tale.index('/w')+1]
        
                tablet[x] = head + tale                 #rebuild the link
                tablet[x] = tablet[x].rstrip('"')       #cleaning it again
                links.append(tablet[x])                 #adding the link to the final list
           
       

    print(links)

###########################################################
def pics_scraper(soup): #need to make a special directory
    
    soup = BeautifulSoup(web.content)

    table = soup.find_all('img')

    for i in range(len(table)):
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


###main

head = 'https://'

URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
web = requests.get(URL)
print(web.status_code)


scrap_links_from_wiki(web)

            
    