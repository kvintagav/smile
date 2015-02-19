from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response,render , get_object_or_404 , redirect
from photo.models import Photographer , Style
from django.utils import timezone
from photo.forms import UserCreationForm , UserChangeForm 
from django.core.context_processors import csrf 
from django.contrib import auth
from django.template import RequestContext

def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password = password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			args['login_error'] = "Пользователь не найден"
			return render(request,'login.html',args)	

	return render(request,'login.html',args)		



def logout(request):
	auth.logout(request)
	return redirect("/")	



def settings(request,user_id):
	args={}
	args.update(csrf(request))
	user = Photographer.object.get(id=user_id)
	args['form']=UserChangeForm(instance = user)
	if request.POST:
		olduser_form = UserChangeForm(request.POST, instance = user)
		if olduser_form.is_valid():
			olduser_form.save()
			return redirect('/office/')
		else:
			args['form'] = olduser_form


	return render(request,'settings.html',args)



def personal(request,user_id):
	args = {}
	args.update(csrf(request))
	return render(request,'personal.html',args)


def office(request):
	args = {}
	args.update(csrf(request))
	return render(request,'office.html',args)


def registration(request):
	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.__init__()
			return redirect('/')
		else:
			args['form'] = newuser_form

	return render_to_response('registration.html',args)		


def search(request):
	args = {}
	args.update(csrf(request))
	#args['form']=PhotographerSearchForm()
	"""if request.POST:
		
		if :
			
			return redirect('/')
		else:
			args['form'] = newuser_form
		"""
			
	return render(request,'search.html',args)
