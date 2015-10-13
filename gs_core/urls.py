from django.conf.urls import url


urlpatterns = [
    url(r'^', 'gs_core.views.home',name='home'),
]
