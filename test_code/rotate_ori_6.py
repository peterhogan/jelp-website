import os, sys
from PIL import Image
from PIL.ExifTags import TAGS

image_input = sys.argv[1]
im = Image.open(image_input)
exif = im._getexif()
if exif[274] == 6:
	im.rotate(270).save()
else:
	pass

