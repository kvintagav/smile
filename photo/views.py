from django.shortcuts import render , get_object_or_404
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from photo.models import Photographer
from django.utils import timezone


def registration(request):
	return HttpResponse("hello registration")

