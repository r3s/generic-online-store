from django.conf.urls import patterns, include, url
from user_profiles import views as profile_view

urlpatterns = patterns('',
    url(r'^login/$', profile_view.UserAuthentication.as_view(), name='login'),
    url(r'^registration/$', profile_view.UserRegistration.as_view(), name='registration'),
    # url(r'^/login/$', 'user_profiles.views.profile_show', name='profile_show'),
    # url(r'^(?P<id>\d+)/calls/$', 'competitions.views.my_calls', name='my_calls'),
)
