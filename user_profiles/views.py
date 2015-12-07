from django.shortcuts import render, redirect
from django.contrib import  auth, messages
from django.views.generic import View
from django import http

from forms import LoginForm

class UserAuthentication(View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('action', '') == "logout":
            auth.logout(request)
            messages.info(request, 'Logout successful..')
        return  render(request, "user_profiles/login.html", {
    		"form": LoginForm,
            })
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, 'Login successful..')
                return redirect('home')
            else:
                messages.success(request, 'Acount not active..')
                return redirect('login')
        else:
            messages.error(request, "Login failed!..")
            return redirect('login')
