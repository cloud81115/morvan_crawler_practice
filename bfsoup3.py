from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg|png')})
for link in img_links:
	print(link['src'])
print('******************')
course_links = soup.find_all('a',{'href':re.compile('https://morvan.*')})
for link in course_links:
	print(link['href'])