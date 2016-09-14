from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

#def logout_user(request):
#	user = request.user.username
#	logout(request)
#	return render(request, 'login/logout.html',{'user': user})

def login_user(request):
	state = "Please log in below:"
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
	
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're logged in successfully."
				return HttpResponseRedirect(reverse('photos:home'))
			else:
				state = "Your account is not active please email peterjameshogan@gmail.com."
		else:
			state = "Your username and/or password is incorrect."

	return render(request,'login/login.html', {'state': state, 'username': username})
