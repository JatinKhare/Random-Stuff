import requests
import numpy as np
from urllib.request import urlopen
import cv2

info = requests.get('https://api.nasa.gov/planetary/apod?api_key=YOUR_NASA_API_KEY').text
date = eval(info)['date']
information = eval(info)['explanation']
title = eval(info)['title']

url = None
try:
	url = eval(info)['hdurl']
except KeyError:
	url = eval(info)['url']
	if 'https:' not in url:
		url = 'https:'+url

print('\n{}\n\n{}\n\n{}\n'.format(title,date,information))

resp = urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Press any key to exit the script after the image is shown.
