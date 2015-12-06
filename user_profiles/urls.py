from django.conf.urls import patterns, include, url
from user_profiles.views import UserAuthentication

urlpatterns = patterns('',
    url(r'^login/$', UserAuthentication.as_view(), name='login'),
    # url(r'^/login/$', 'user_profiles.views.profile_show', name='profile_show'),
    # url(r'^(?P<id>\d+)/calls/$', 'competitions.views.my_calls', name='my_calls'),
)
