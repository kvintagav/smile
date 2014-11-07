from django.conf.urls import patterns, include, url

from photo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ntmusic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registration/$', views.registration, name='registration'),
   # url(r'^$', views.registration, name='registration'),

)
