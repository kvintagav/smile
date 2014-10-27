from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime

class Photographer(Models.model):
	class Meta():
		db_table = 'Photographer'
	first_name = models.CharField(_(u'first_name '),max_length=100)
	second_name = models.CharField(_(u'second_name '),max_length=100)
	login = models.CharField(_(u'login'),max_length=100)
	about = models.TextField(_(u'about'))
	date_registration =  models.DateTimeField(_(u'date_registration'))
	date_pay =  models.DateTimeField(_(u'date_pay'))
	#type_account =	
	
	def __unicode__(self):
		return self.name
	


class PhotoExample(object):
	"""Example foto """
	
	def __init__(self, arg):
		super (PhotoExample, self).__init__()
		self.arg = arg
	

class Action(object):
	"""Photographer can create action with date"""

	def __init__(self, arg):
		super(Action, self).__init__()
		self.arg = arg
		

class Sale(object):
	"""Photographer can create sale on his work"""

	def __init__(self, arg):
		super(Sale, self).__init__()
		self.arg = arg
		
class Location(object):
	"""Location Photographer"""
	
	country = models.CharField(_(u'country'),max_length=100)
	region = models.CharField(_(u'region '),max_length=100)
	city = models.CharField(_(u'city '),max_length=100)

	def __init__(self, arg):
		super(Location, self).__init__()
		self.arg = arg
		