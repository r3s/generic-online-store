from django.shortcuts import render
from django import http

# function based view example
def home(request):
    return http.HttpResponse( "You have arrived at home .. ")
