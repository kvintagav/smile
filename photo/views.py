from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response,render , get_object_or_404 , redirect
from photo.models import Photographer
from django.utils import timezone
from photo.forms import UserCreationForm
from django.core.context_processors import csrf 

"""
def login(request):
	pass

def  logout(request):
	pass


"""


def registration(request):
	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm[request.POST]
		if newuser_form.is_valid():
			newuser_form.save()
			return redirect('/')
		else:
			args['form'] = newuser_form
	return render_to_response('registration.html',args)		
