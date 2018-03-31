#download files
import os 
os.makedirs('./img/',exist_ok=True)
IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
#use urlretrieve
"""from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'./img/imge1.png')"""

#use request
import requests
"""r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
	f.write(r.content)"""

r = requests.get(IMAGE_URL, stream=True)
with open('./img/image3.png','wb') as f:
	for chunk in r.iter_content(chunk_size=32):
		f.write(chunk)

