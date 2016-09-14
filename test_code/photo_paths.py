from os.path import join
from os.path import basename

from glob import glob

path = '/home/pine/Dropbox'
#files_jpg = '/home/pine/Dropbox/Camera Uploads/*.jpg'
#files_JPG = '/home/pine/Dropbox/Camera Uploads/*.JPG'
files_jpg = '/home/pine/Dropbox/*.jpg'
files_JPG = '/home/pine/Dropbox/*.JPG'

photo_paths = glob(join(files_jpg,files_JPG))
photo_names = [basename(file) for file in photo_paths]

dj_photos = zip(photo_names,photo_paths)

for i in dj_photos:
	print(i)

print(photo_paths[1])
photo_paths[3]
