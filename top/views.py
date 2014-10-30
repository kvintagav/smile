from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
# Create your views here.


def index(request):
    return render_to_response('index.html')



