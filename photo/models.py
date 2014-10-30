from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser)
from datetime import datetime


class MyUserManager(BaseUserManager):
	def create_user(self,email,username,password= None):

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			)

		user.self_password(password)
		user.save (using=self._db)

		return user


class Photographer(AbstractBaseUser):
	email = models.EmailField(_(u'email'),max_length=255,unique=True)
	about = models.TextField(_(u'about'))
	date_birth = models.DateTimeField(_(u'date_birth')) 
	date_pay =  models.DateTimeField(_(u'date_pay'))
	about_short = models.TextField(_(u'about_short'))
  
	def __unicode__(self):
		return self.name
	
	object = MyUserManager()
	




"""		
class Location(object):
	
	country = models.CharField(_(u'country'),max_length=100)
	region = models.CharField(_(u'region '),max_length=100)
	city = models.CharField(_(u'city '),max_length=100)
"""
