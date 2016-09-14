from sys import argv
from PIL import Image
from PIL.ExifTags import TAGS
from getopt import getopt
import os, glob

path_arg = argv[1]

print("Reading :",os.path.realpath(path_arg),'...\n')

path = os.path.realpath(path_arg)
img = Image.open(path)
exif_data = img._getexif()

for i in exif_data:
	print(i,'-',TAGS[i],':'),
	print(exif_data[i]),

#size = 128,128
#img.thumbnail(size)
#img.save("jasper-thumb.jpg", "JPEG")
#os.system("feh "+path)
