from django.conf.urls import *

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', profile_index, name='profile_index'),
    url(r'(?P<id>\d+)/$', profile, name='profile_detail'),
)
