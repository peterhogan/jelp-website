from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from random import randint

import datetime
from photos.models import Photo

# for photos
from datetime import datetime
from os.path import join
from os.path import basename
from os import listdir
from glob import glob
from random import sample

#def login_screen(request):
#	html = "<html><body><form> Enter the passphrase:<br><input type='text' name='passphrase'><input type='submit' value='Submit'></form></body></html>"
#	return HttpResponse(html)

@login_required(login_url='login:login')
def logout_user(request):
	user = request.user.username
	logout(request)
	return render(request, 'photos/logout.html',{'user': user})

@login_required(login_url='login:login')
def years(request):
	username = request.user.username
	years = []

	for file in Photo.objects.all():
		if file.date_created.strftime('%Y') in years:
			pass
		else:
			years.append(file.date_created.strftime('%Y')) 

	photo_from_year = []
	yearnum_for_year = []
	for year in sorted(years):
		selector = randint(0,len(Photo.objects.filter(date_created__year=year))-1)
		photo_from_year.append(Photo.objects.filter(date_created__year=year)[selector])
		yearnum_for_year.append(year)
	photos_with_years = zip(yearnum_for_year,photo_from_year)

	context = {'years': sorted(years), 'photos_with_years': photos_with_years,'username': username  }
	return render(request, 'photos/years.html', context)

@login_required(login_url='login:login')
def months(request, year):
	username = request.user.username
	months = []

	for i in Photo.objects.filter(date_created__startswith=year):
		if i.date_created.strftime('%m') in months:
			pass
		else: 
			months.append(i.date_created.strftime('%m'))

	months_new = [datetime.strftime(datetime.strptime(i,'%m'),'%b') for i in sorted(months)]

	photo_from_month = []
	month_name = []
	for month in months_new:
		month_number = datetime.strftime(datetime.strptime(month,"%b"),"%m")
		selector = randint(0,int(len(Photo.objects.filter(date_created__year=year).filter(date_created__month=month_number)))-1)
		photo_from_month.append(Photo.objects.filter(date_created__year=year).filter(date_created__month=month_number)[selector])
		month_name.append(month)#datetime.strftime(datetime.strptime(month,"%b"),"%b"))

	month_pairs = zip(month_name,photo_from_month)
	

	return render(request, 'photos/months.html', {'username': username, 'year': year, 'months': month_pairs})

@login_required(login_url='login:login')
def photos(request, year, month):
	username = request.user.username

	mnth = datetime.strftime(datetime.strptime(month, '%b'),'%m')
	photos_of_month = Photo.objects.filter(date_created__year=year).filter(date_created__month=mnth)
	photo_paths = [i.title for i in Photo.objects.filter(date_created__year=year).filter(date_created__month=mnth)]

	context = {'photo_paths': photo_paths,'year': year, 'month': month, 'username': username}
	return render(request, 'photos/photos.html', context)

@login_required(login_url='login:login')
def photo_detail(request,year, month, title):
	username = request.user.username
	orientation = Photo.objects.get(title=title).orientation
	timetaken = Photo.objects.get(title=title).time_created
	datetaken = Photo.objects.get(title=title).date_created

	context = {'title': title,'year': year, 'month': month, 'time': timetaken, 'date': datetaken, 'ori':orientation,'username': username}
	return render(request, 'photos/photo_detail.html', context)
	
@login_required(login_url='login:login')
def home(request):
	username = None
	if request.user.is_authenticated():
		username = request.user.username
	context = {'username':username}
	return render(request, 'photos/home.html', context)

@login_required(login_url='login:login')
def random(request):
	username = request.user.username
	random_photo = sample(list(Photo.objects.all().values('title')),1)[0]
	title = random_photo['title']
	year = datetime.strftime(Photo.objects.get(title=title).date_created, '%Y')
	month = datetime.strftime(Photo.objects.get(title=title).date_created, '%B')
	orientation = Photo.objects.get(title=title).orientation
	timetaken = Photo.objects.get(title=title).time_created
	datetaken = Photo.objects.get(title=title).date_created
	
	context = {'title': random_photo['title'],'year': year, 'month': month, 'time': timetaken, 'date': datetaken, 'ori':orientation,'username': username}
	return render(request, 'photos/random.html', context)

@login_required(login_url='login:login')
def latest(request):
	username = request.user.username
	latest_photos_list = Photo.objects.order_by('-date_created')[:20]
	phototitles = []
	photoyears = []
	photomonths = []

	for i in latest_photos_list:
		phototitles.append(i.title)
		photomonths.append(datetime.strftime(i.date_created,'%b'))
		photoyears.append(datetime.strftime(i.date_created,'%Y'))

	photodetails = zip(phototitles,photoyears,photomonths)

	context = {'latest_photos': photodetails,'username': username}
	return render(request, 'photos/latest.html', context)
