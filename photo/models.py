
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser)
from datetime import datetime


class MyUserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		email = self.normalize_email(email)	
		Photographer = self.model(email=email,username=username,)
		Photographer.set_password(password)
		Photographer.save(using=self._db)
		return Photographer

	def create_superuser(self, email, username, password):
		Photographer = self.create_user(email,password=password,username=username)
		Photographer.is_admin = True
		Photographer.save(using=self._db)
		return Photographer

class Photographer(AbstractBaseUser):
	email = models.EmailField(_(u'email'),max_length=255,unique=True)
	username = models.CharField(_(u'user_name'), max_length= 30, unique= True)
	#avatar
	first_name = models.CharField(_(u'first_name'), max_length= 30, unique= False)
	second_name = models.CharField(_(u'second_name'), max_length= 30, unique= False)
	about = models.TextField(_(u'about'))
	date_birth = models.DateTimeField(_(u'date_birth') , blank=True, null=True) 

	date_pay =  models.DateTimeField(_(u'date_pay'),  blank=True, null=True)
	is_active = models.BooleanField(default=True)

	is_admin = models.BooleanField(default=False)

	sity = models.CharField(_(u'first_name'), max_length= 30, unique= False)

	max_sale = models.IntegerField(default=3)
	max_action = models.IntegerField(default=3)
	max_style = models.IntegerField(default=3)


	#type_accaunt = models.CharField(_(u'type_accaunt'),max_length = 30)

	#mounts_foto = models.IntegerField(_(u'mount_foto'))
	#mounts_teg = models.IntegerField(_(u'mount_teg'))


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


	object = MyUserManager()


	def get_full_name(self):
		return '%s %s' % (self.first_name, self.last_name,)

	def get_short_name(self):
		return self.username

	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin


class Style(models.Model)

	FAMILY = 'FM'
    PORTRAIT = 'PO'
    ALL_STYLE_CHOICES = (
        (FAMILY, 'Семья'),
        (PORTRAIT, 'Портрет'),
       
    )
	style_work = models.CharField(max_length=30,choices=ALL_STYLE_CHOICES,default=PO)
	photographer = models.ForeignKey(Photographer)


class Action(models.Model)
	photographer = models.ForeignKey(Photographer)

class Sale(models.Model)
	photographer = models.ForeignKey(Photographer)

class Location(models.Model)

