from django.conf.urls import patterns, include, url

from photo import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ntmusic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^settings/(?P<user_id>\d+)/$', views.settings, name='settings'),
    
   # url(r'^$', views.registration, name='registration'),

)
