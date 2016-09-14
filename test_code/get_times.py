from glob import glob
from os.path import basename
import datetime

files = glob('/home/pine/python/django/mysite2/photos/static/photos/*.jpg')
filenames = [basename(i) for i in files]
times = []

for i in filenames:
	try:
		times.append(str(datetime.datetime.strptime(i, '%Y-%m-%d %H.%M.%S.jpg')))
	except ValueError:
		try:
			times.append(str(datetime.datetime.strptime(i, '%Y-%m-%d_%H.%M.%S.jpg')))
		except ValueError:
			print('Could not process %s.' % i)
print(times)
