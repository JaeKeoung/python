#web scraping code
from bs4 import BeautifulSoup
import urllib.request
response=urllib.request.urlopen('http://www.inven.co.kr/board/powerbbs.php?come_idx=4485')
page=response.read().decode('utf-8', 'ignore')
#print (page)
soup=BeautifulSoup(page, 'html5lib')
#print (soup)
list=soup.findAll('td',attrs={'class':'bbsSubject'})
for item in list:
    title=item.find('a').text
    print(title)
