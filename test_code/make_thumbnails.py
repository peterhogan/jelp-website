import os, sys
from glob import glob
from PIL import Image

size = (128,128)

files = glob(sys.argv[1]+"/*.jpg")

for i in files:
	output = sys.argv[2] + os.path.basename(i)
	print(output)
	if i != output:
		try:
			im = Image.open(i)
			im.thumbnail(size)
			im.save(output,"JPEG")
		except IOError:
			print("cannot create thumbnail for", i)


############################################################################################
	#output = os.path.splitext(i)[0] + '.jpg'
	#output = os.path.dirname(i) + '/thumbnails/' + os.path.basename(os.path.splitext(i)[0]) + '.thumb'
