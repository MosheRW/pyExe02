from itertools import count
import requests
from bs4 import BeautifulSoup
import bs4
import os
from datetime import datetime

def is_home_page(url):
    web = requests.get(url)
    #if web.status_code == True:
    if web.ok == True:
        return   get_the_page_name(web) == 'עמוד ראשי' 
    else:
        return False
 

#--------------         picture naming functions            -------------------
def strip_slash(txt):
    txt = txt.strip('"')
    
    if txt.rfind('/') != -1:
        return txt[txt.rfind('/')+1:]
    else:
        return txt
    
def strip_dots(txt):
    if txt.count('.') > 1:
         return txt[txt.find('.')+1:]
    
    return txt
    
def pic_the_name(tale):
     img_name = tale.partition('px-')
     
     if img_name.count('px-') != 0:
         return img_name[img_name.index('px-')+1]
     else:
         return img_name[0]
    
def pic_name(tale):
    #return strip_dots(strip_slash(pic_the_name(tale)))         # i prefer the long form' for clarity

    txt = pic_the_name(tale)
    txt = strip_slash(txt)
    txt = strip_dots(txt)
    
    print(txt)
    return txt
    
#--------------         picture scraping function           -------------------
"""
    there is three data-sets
    1. imgTable: contains all implementations of images 
    2. txt: contains the splited txt of the cueernt implementation
    3. tablet: contains a set of images (usually from a single class, usually number of sizes of the same picture)
"""
def pics_scraper(web, max_pics = 25, file_name = None):  #pics scraper
    head = 'https://'
    count_pics = 0
    
    soup = BeautifulSoup(web.content,features="html.parser")

    imgTable = soup.find_all('img')

    for i in range(len(imgTable)):                      # loop over all pics links
    
        txt = str(imgTable[i])
        txt = txt.split()

        tablet = list()                                 # creat a list

    
        for x in range(len(txt)):                       # Puts the drity pics links in the temp tablet list
            if txt[x].count('//upload') != 0:
                tablet.append(txt[x])       
            
        #print(tablet)
            
        for x in range(len(tablet)):
            tale = tablet[x].partition('//')
            tale = tale[tale.index('//')+1]

            tablet[x] = head + tale                    #
            tablet[x] = tablet[x].strip('"')
            
            if x == len(tablet)-1 and tablet[x].count("svg") == 0:  
                #img_name = pic_name(tale)            
                img_data = requests.get(tablet[x]).content
                with open(pic_name(tale), 'wb') as handler:
                    handler.write(img_data)
                    
                count_pics += 1
                
            #if count_pics >= max_pics:
            if len(next(os.walk(os.getcwd()))[2]) >= max_pics:
                break;
        
        #if count_pics >= max_pics:
        if len(next(os.walk(os.getcwd()))[2]) >= max_pics:
            break;

               
#--------------         links scraping function             -------------------
def links_scraper(web, max_childes = 5, file_name = None):  #links scraper
    
    counter = 0
    
    head = 'https://he.wikipedia.org'

    soup = BeautifulSoup(web.text, 'html.parser')

    table = soup.find_all('p')

    links = list()

    for i in range(len(table)): 
      
        txt = str(table[i])       
        txt = txt.split()

        tablet = list()                                     #creat a list
    
    
        for x in range(len(txt)):
            if txt[x].count("href=") != 0 and txt[x].count("mw-redirect") == 0 and txt[x].count("index") == 0 and txt[x].count("עמוד ראשי") == 0 and txt[x].count("פורטל") == 0 and txt[x].count(":") == 0 and txt[x].count("mp3") == 0:                  #Puts the drity links in the temp tablet list
                tablet.append(txt[x])       
    
     
        
        for x in range(len(tablet)):                        #cleaning the link
            
            tablet[x] = tablet[x].replace('href=',head)
            tablet[x] = tablet[x].replace('"','')
            print(tablet[x])
          #  tale = tablet[x].partition('/w')
           
            if tablet[x].count('wiki') >= 1 and tablet[x].count('href') == 0 and not is_home_page(str(tablet[x])):
                links.append(tablet[x])                     #adding the link to the final list
                counter = counter + 1   
          
        if counter >= max_childes * 2: break
    
       

    #print(links)
    return links

#--------------         get the web page name               -------------------
def get_the_page_name(web):
  
    soup = BeautifulSoup(web.text, 'html.parser')

    table = soup.find_all('span', attrs={'class':'mw-page-title-main'})
    
    #if len(table) >= 0:
    if len(table) >= 0:
        try:
            txt = str(table[0])
        except:
         raise Exception("Sorry, no numbers below zero")
    
    #txt = txt[txt.find('>')+1:txt.rfind('<')]
    return  txt[txt.find('>')+1:txt.rfind('<')].replace('"','')
    
def folder_heandler(txt, status = "start"):
    prev = os.getcwd()
 
    if status == "start" and not os.path.exists(txt):
        os.mkdir(txt)
        os.chdir(txt)
        return prev
    
    else:
         os.chdir(txt)     
         return prev
    
def web_crawler(url = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C', num_of_pages = 5, max_pics = 25, num_of_jumps = 5):
    
    print(url)

    if num_of_jumps == 0:
        return True
    
    web = requests.get(url)
    print(web.status_code)
    
    if not web.ok: return False
    
    try:
        name = get_the_page_name(web)
    except:
        return False
    
    print(name)
    
    folder_path = folder_heandler(name, "start")

    pics_scraper(web,max_pics)
    
    folder_path = folder_heandler(folder_path, "end")
    
    
    links_list = links_scraper(web,num_of_pages)
    
    count = 0
    
    for link in links_list:
       # if count != 0: folder_path = folder_heandler(folder_path, "end")
       # count = count + 1
        if count > num_of_pages: break   
        print(link)
        if web_crawler(link,num_of_pages,max_pics,num_of_jumps-1):
            count = count + 1
        #    folder_path = folder_heandler(folder_path, "end")
        else:
            continue
            #return web_crawler(link,num_of_pages,max_pics,num_of_jumps-1)
            

            
    #folder_path = folder_heandler(folder_path, "end")
    
    return True
            
 
def creat_father_directory(copys = 0, now = datetime.now()):
    
    if copys == 0:
        name = now.strftime("%d_%m_%Y-%H%M%S")
    else:
        name = now.strftime("%d_%m_%Y-%H%M%S") + '_0' + str(copys)
            
    if os.path.exists(name):
        creat_father_directory(copys + 1,now)
    else:
         os.mkdir(name)
         os.chdir(name)
        
            
   
    

   

###########################################################
    
###main

#URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
#URL = 'https://he.wikipedia.org/wiki/%D7%95%D7%99%D7%A0%D7%A1%D7%A0%D7%98_%D7%95%D7%90%D7%9F_%D7%92%D7%95%D7%9A'
#URL = 'https://he.wikipedia.org/wiki/%D7%91%D7%A0%D7%99%D7%9E%D7%99%D7%9F_%D7%A0%D7%AA%D7%A0%D7%99%D7%94%D7%95'




#web_crawler(URL,2,3,5)

def user_input():
    url = input("copy and past a hebrew wikiPedia link: ")
    
    num_of_pages = int(input("insert the number of pages to scrap from any page: "))
    while num_of_pages < 1:
	    num_of_pages = int(input("The insertsd value does not match. try again: ")) 
        
    num_of_picts = int(input("insert the number of pics to scrap from any page: "))
    while not 1 <= num_of_picts <= 30 :
	    num_of_picts = int(input("The insertsd value does not match. try again: ")) 
        
    num_of_jumps = int(input("insert the number of jumps: "))
    while not 1 <= num_of_jumps <= 10 :
	    num_of_jumps = int(input("The insertsd value does not match. try again: ")) 
    
    web_crawler(url,num_of_pages,num_of_picts,num_of_jumps)



creat_father_directory()
#user_input()
        
"""
folder = os.getcwd()
print(folder)
lst = os.listdir(folder) # your directory path
number_files = len(lst)
print(number_files)
onlyfiles = next(os.walk(folder))[2] #directory is your directory path as string
print(len(onlyfiles))
"""