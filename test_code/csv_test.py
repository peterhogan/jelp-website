#
# This script will create a csv of all the details of all the photos in a directory
# To use the script you must run python script_name.py csv_to_output.csv /dir/of/photos/
#

from PIL import Image
from PIL.ExifTags import TAGS
from glob import glob
import os,  csv, sys

f = open(sys.argv[1], 'wt')

dir_path = sys.argv[2]

print("Reading all files in %s and outputting csv as %s." %(dir_path, os.path.realpath(sys.argv[1])))

all_file_paths = glob(dir_path+"*.jpg")
filenames = [os.path.basename(i) for i in all_file_paths]
datetime_created = []
orientation = []

for i in all_file_paths:
	img = Image.open(i)
	exif_data = img._getexif()
	try:
		ori = exif_data[274]
		datet_cr = exif_data[36867]
	except TypeError:
		ori = "NA"
		datet_cr = "NA NA"
	finally:
		datetime_created.append(datet_cr)
		orientation.append(ori)

dates_created = [i.split()[0] for i in datetime_created]
times_created = [i.split()[1] for i in datetime_created]

all_data = zip(filenames,dates_created,times_created,datetime_created,orientation,all_file_paths)


try:
    writer = csv.writer(f)
    writer.writerow( ('title', 'date_created', 'time_created', 'datetime_created','orientation','path') )
    for i in all_data:
        writer.writerow( (i[0],i[1],i[2],i[3],i[4],i[5]))
finally:
    f.close()

print(open(sys.argv[1], 'rt').read())
