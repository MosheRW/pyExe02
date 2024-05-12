import requests
from bs4 import BeautifulSoup
import bs4

URL = 'https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C'
web = requests.get(URL)
print(web.status_code)
soup = BeautifulSoup(web.content)

section = soup.find('body')
"""
section = section.find('div', attrs={'class': 'mw-page-container-inner'})
section = section.find('main', attrs={'id': 'content', 'class':'mw-body', 'role':'main'})
section = section.find('div', attrs={'id': 'bodyContent'})
section = section.find('div', attrs={'id': 'mw-content-text'})
section = section.find('div', attrs={'class': 'mw-content-rtl mw-parser-output'})#maybe need to do that in a loop
#section = section.find('figure', attrs={'typeof': 'mw:File/Thumb'})

section = section.find('a', attrs={'class': 'mw-file-description'})
"""
#section = section.find_all('a', attrs={'class': 'mw-file-description'})

#section = soup.find('img')
table = soup.find_all('img')
section = table[47]

#'div' id:bodyContent

#print(len(table))
#print(len(section))
#print(section)

txt = str(section)
x = txt.find("src=")

print(txt)
print(x)
print(txt[x])

x1 = txt.find('"',x+6)

#print(txt)
print(x1)
print(txt[x1])

txt1 = txt.split()
print(txt1)

tablet = list()
for i in range(len(txt1)):
    print(f"i: {i}: \n")
    print(txt1[i])
    print("\n")
  
print(txt1.count('//upload'))
for i in range(len(txt1)):    
    if txt1[i].count('//upload') != 0:
 #   if txt1[i].find('//upload'):
        tablet.append(txt1[i])       
        print(f"i: {i}: true")
    else:
        print(f"i: {i}: false")
    
for i in range(len(tablet)):    
        print(f"i: {i}: {tablet[i]}")
        
head = 'https://'

for i in range(len(tablet)):    
    tale = tablet[i].partition('//')[2]
    tablet[i] = head + tale
    tablet[i] = tablet[i].rstrip('"')
    print(tablet[i])

    img_name = str(i) + '.jpg'
    img_data = requests.get(tablet[i]).content
    with open(img_name, 'wb') as handler:
        handler.write(img_data)