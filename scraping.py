#web scraping code
from bs4 import BeautifulSoup
import urllib.request
response=urllib.request.urlopen('http://www.clien.net/cs2/bbs/board.php?bo_table=news')
page=response.read().decode('utf-8', 'ignore')
#print (page)
soup=BeautifulSoup(page, 'html5lib')
#print (soup)
list=soup.findAll('td',attrs={'class':'post_subject'})
for item in list:
    title=item.find('a').text
    print(title)
