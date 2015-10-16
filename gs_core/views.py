from django.shortcuts import render
from django import http
import logging
from django.conf import settings


# globals
if not settings.DEBUG:
    logger = logging.getLogger("django.request")
else:
    logger = logging.getLogger("gs_file")


# function based view example
def home(request):
    return http.HttpResponse( "You have arrived at home .. ")
