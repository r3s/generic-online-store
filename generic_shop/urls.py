from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/shop/', include('shop.admin_urls')),
    url(r'^auth/', include('user_profiles.urls')),
    url(r'^', include('gs_core.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


## debug stuff to serve static media
# from django.conf import settings
# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT}),
#    ]
