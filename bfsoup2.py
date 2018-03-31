from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')


jan = soup.find('ul',{'class' :'jan'})
#print(jan)
d_jan = jan.find_all('li')
for d in d_jan:
	print(d.get_text())

#another way
ajan = soup.find_all('ul',{'class' :'jan'})
for d in ajan:
	print(d.get_text())