from django.conf.urls import url
from gs_admin import views as admin_view


urlpatterns = [
    url(r'^$', admin_view.AdminHome.as_view(), name='admin_home'),
]
