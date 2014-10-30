from django.contrib import admin
from photo.models import Photographer

# Register your models here.
"""
class PhotographerAdmin(admin.ModelAdmin):
	fields =  ['login','date_registration']
	list_display = ('login', 'date_registration')
	list_filter = ['date_registration']
"""

admin.site.register(Photographer)