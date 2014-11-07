from django.conf.urls import patterns, include, url
from django.contrib import admin
from photo.views import registration

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywaysmile.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^registration/',include('photo.urls',namespace="photo")),
    url(r'^registration/',registration,name="registration"),
 	url(r'^$', include('top.urls',namespace="top")),
    	   
)
