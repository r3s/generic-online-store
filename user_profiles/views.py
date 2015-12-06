from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django import http
from forms import LoginForm

class UserAuthentication(View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('action', '') == "logout":
            logout(request)
        return  render(request, "user_profiles/login.html", {
    		"form": LoginForm,
            })
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return http.HttpResponse( "Login success.. ")
            else:
                return http.HttpResponse( "Acount not active.. ")
        else:
            return http.HttpResponse( "Err.. ")
