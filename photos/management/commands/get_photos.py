from django.core.management.base import BaseCommand
from photos.models import Photo
from PIL import Image
from PIL.ExifTags import TAGS
from glob import glob
import os, sys, fnmatch
from datetime import datetime
from logging import info,debug,error,basicConfig,DEBUG

basicConfig(filename='getphotos-logfile.log', level=DEBUG)

# Setting up the error counters
# photos_added
# photos_failed
# photos_skipped
# thumbnails_made
# thumbnails_failed 
# photos_spun

# Where to look for photos
basepath = '/home/pine/python/django/mysite2/photos/static/photos/'
# Where the thumbnails are stored INCLUDE '/' at the end
thumbnail_path = '/home/pine/python/django/mysite2/photos/static/photos/thumbnails/'


class Command(BaseCommand):
	help = 'Pulls all the photos from /static/photos/ and puts their details in the database'

	def handle(self, *args, **options):
###############################################
#####    Set Thumbnail Size Here (size):         #####
###############################################
		size = (128,128)
		info("Size variable for thumbnails is set to %r" % str(size))
		photos_added = 0
		photos_failed = 0
		photos_skipped = 0
		thumbnails_made = 0
		thumbnails_failed = 0
		photos_spun = 0
		all_file_paths = []
		for root, dirnames, filenames in os.walk(basepath):
			if fnmatch.fnmatch(root,'*/thumbnails'):
				info("Found '*/thumbnails' - Breaking loop at %s" % root) 
				break
			for filename in fnmatch.filter(filenames, '*.jpg'):
				all_file_paths.append(os.path.join(root, filename))
				info("Added %s to all_file_paths list." % os.path.join(root, filename))

		filenames = [os.path.basename(i) for i in all_file_paths]
		datetime_created = []
		orientation = []

		for i in all_file_paths:
			img = Image.open(i)
			exif_data = img._getexif()
			try:
				ori = exif_data[274]
				try:
					datet_cr = exif_data[36867].replace(':','-',2)+'+00:00'
				except KeyError:
					debug("Key error for file %s when trying to find date created" % i)
					try:
						datet_cr = str(datetime.strptime(os.path.basename(i),'%Y-%m-%d_%H.%M.%S.jpg')).replace('_',' ',1)
					except ValueError:
						debug("Value error for file %s when trying to find date created" % i)
						try:
							datet_cr = str(datetime.strptime(os.path.basename(i),'%Y-%m-%d %H.%M.%S.jpg'))
						except (KeyboardInterrupt, SystemExit):
							debug("Legit exception (Did you press Ctrl-C?)")
							raise
			except TypeError:
				debug("No orientation or datetime found so assigning orientation=0 and date_created=000-00-00 00:00")
				ori = "0"
				datet_cr = "0000-00-00 00:00+00:00"
			except:
				error("Unidentified error when trying to add photo %s, try adding manually." % i)
				pass
			finally:
				datetime_created.append(datet_cr)
				orientation.append(ori)
				info("collected date created and orientation to database for %s" % i)

		dates_created = [i.split()[0] for i in datetime_created]
		times_created = [i.split()[1] for i in datetime_created]

		all_data = zip(filenames,dates_created,times_created,datetime_created,orientation,all_file_paths)
		info("All data zipped")

		#details = "title=i[0],date_created=i[1],time_created=i[2],datetime_created=i[3],orientation=i[4],path=i[5]"

		try:
			for i in all_data:
				if Photo.objects.filter(path=i[5]).exists():
					photos_skipped += 1
					info("Photo %s already in the database, skipping" % i[5])
					pass
				else:
					info("Photo not in the database yet")
					photos_added += 1
					# open the photo first 
					img = Image.open(i[5])
					# check orientation and if it's 6 then flip it around 270 deg
					if i[4] == 6:
						info("orientation not correct, rotating %s by 270 deg" % i[0])
						photos_spun += 1
						img.rotate(270).save(i[5])
					try:
						output = thumbnail_path + os.path.basename(i[5])
						debug("Thumbnail file path is %s with output %s" % (thumbnail_path, output))
						img.thumbnail(size)
						img.save(output, 'JPEG')
						thumbnails_made += 1
					except IOError:
						debug("IO error - check file path in logs")
						thumbnails_failed +=1
						pass
					except:
						thumbnails_failed +=1
						error("THUMBNAIL NOT ADDED - YOU MUST ADD %s MANUALLY AS A THUMBNAIL" % i[0])
						pass
					info("Adding: %s to the database" % i[5])
					Photo.objects.create(title=i[0],date_created=i[1],time_created=i[2],datetime_created=i[3],orientation=i[4],path=i[5])
					photos_added +=1

		except (KeyboardInterrupt, SystemExit):
			debug("Legit exception (Did you press Ctrl-C?)")
			photos_failed += 1
			raise
		except:
			info('Skipping %s with an unidentified error' % i[0])
			photos_failed += 1
			pass

		total_photos = Photo.objects.all().count()
		info('Total photos: %i' % total_photos)
		info('Photos added: %i' % photos_added)
		info('Photos skipped: %i' % photos_skipped)
		info('Photos failed: %i' % photos_failed)
		info('Photos rotated: %i' % photos_spun)
		info('Thumbnails made: %i' % thumbnails_made)
		info('Thumbnails failed: %i' % thumbnails_failed)
		self.stdout.write('Total photos: %i' % total_photos)
		self.stdout.write('Photos added: %i' % photos_added)
		self.stdout.write('Photos skipped: %i' % photos_skipped)
		self.stdout.write('Photos failed: %i' % photos_failed)
		self.stdout.write('Photos rotated: %i' % photos_spun)
		self.stdout.write('Thumbnails made: %i' % thumbnails_made)
		self.stdout.write('Thumbnails failed: %i' % thumbnails_failed)


