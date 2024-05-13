import requests
from bs4 import BeautifulSoup
import bs4

def pics_scraper(web):                                  #pics scraper
    
    soup = BeautifulSoup(web.content)

    table = soup.find_all('img')

    for i in range(len(table)):
    
        txt = str(table[i])
        txt = txt.split()

        tablet = list()                                 #creat a list

    
        for x in range(len(txt)):                       #Puts the drity pics links in the temp tablet list
            if txt[x].count('//upload') != 0:
                tablet.append(txt[x])       
    
        for x in range(len(tablet)):
            tale = tablet[x].partition('//')
            tale = tale[tale.index('//')+1]

            tablet[x] = head + tale                    #
            tablet[x] = tablet[x].rstrip('"')
            print(tablet[x])

            img_name = str(i) + '_' + str(x) + '.jpg'  
            img_data = requests.get(tablet[x]).content
            with open(img_name, 'wb') as handler:
                handler.write(img_data)


#################
def links_scraper(web):                                 #links scraper
    
    head = 'https://he.wikipedia.org/w'

    soup = BeautifulSoup(web.text, 'html.parser')

    table = soup.find_all('p')

    links = list()

    for i in range(len(table)): 
      
        txt = str(table[i])       
        txt = txt.split()

        tablet = list()                                 #creat a list
    
    
        for x in range(len(txt)):
            if txt[x].count("href=") != 0:              #Puts the drity links in the temp tablet list
                tablet.append(txt[x])       
    
     
          
        for x in range(len(tablet)):                    #cleaning the link
            
            tale = tablet[x].partition('/w')
            
            if tale.count('/w') != 0:
                tale = tale[tale.index('/w')+1]
        
                tablet[x] = head + tale                 #rebuild the link
                tablet[x] = tablet[x].rstrip('"')       #cleaning it again
                links.append(tablet[x])                 #adding the link to the final list
           
       

    #print(links)
    return links

###########################################################


###main

head = 'https://'

URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
web = requests.get(URL)
print(web.status_code)


pics_scraper(web)

            
    