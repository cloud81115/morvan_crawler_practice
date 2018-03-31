import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re
from multiprocessing import Process 
from multiprocessing import freeze_support

base_url = 'https://morvanzhou.github.io/'
if base_url !="http://127.0.0.1:4000/":
	restricted_crawl = True
else:
	restricted_crawl = False
def crawl(url):
	response = urlopen(url)
	return response.read().decode()
def parse(html):
	soup = BeautifulSoup(html, 'lxml')
	urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
	title = soup.find('h1').get_text().strip()
	page_urls = set([urljoin(base_url, url['href'])for url in urls])
	url = soup.find('meta', {'property': "og:url"})['content']
	return title, page_urls, url
"""unseen = set([base_url,])
seen = set()
count, t1=1,time.time()

while len(unseen)!= 0:
	if restricted_crawl and len(seen)>20:
		break 
	print('\nDistributed Crawling...')
	htmls = [crawl(url) for url in unseen]
	print('\nDistributed Parsing...')
	results = [parse(html) for html in htmls]
	print('\nAnalysing...')
	seen.update(unseen)
	unseen.clear()
	for title, page_urls, url in results:
		print(count, title, url)
		count += 1
		unseen.update(page_urls - seen)
print('Total time:%.1f s' % (time.time()-t1, ))"""

#multiprocessing

unseen = set([base_url,])
seen = set()
count, t1=1,time.time()
if __name__ == '__main__':

	pool = mp.Pool(4)
	while len(unseen)!= 0:
		if restricted_crawl and len(seen)>20:
			break 
		print('\nDistributed Crawling...')
		crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
		htmls = [j.get() for j in crawl_jobs]
		print('\nDistributed Parsing...')
		parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
		results = [j.get() for j in parse_jobs]
		print('\nAnalysing...')
		seen.update(unseen)
		unseen.clear()
		for title, page_urls, url in results:
			print(count, title, url)
			count += 1
			unseen.update(page_urls - seen)     
	print('Total time: %.1f s' % (time.time()-t1, ))