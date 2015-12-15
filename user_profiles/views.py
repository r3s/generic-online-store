from django.shortcuts import render, redirect
from django.contrib import  auth, messages
from django.views.generic import View
from django import http

import forms as profile_forms
from django.contrib.auth.models import User



class UserAuthentication(View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('action', '') == "logout":
            auth.logout(request)
            messages.info(request, 'Logout successful..')
        return  render(request, "user_profiles/login.html", {
    		"form": profile_forms.LoginForm,
            'reg_form': profile_forms.RegForm
            })
    def post(self, request, *args, **kwargs):
        form = profile_forms.LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
            password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Login successful..')
                    return redirect('home')
                else:
                    messages.error(request, 'Acount not active..')
                    return redirect('login')
        messages.error(request, "Login failed!..")
        return  render(request, "user_profiles/login.html", {
    		"form": form,
            'reg_form': profile_forms.RegForm
            })

class UserRegistration(View):
    def post(self, request, *args, **kwargs):
        form = profile_forms.RegForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(first_name=form.cleaned_data['name'],
                                            username=form.cleaned_data['username'],
                                             email=form.cleaned_data['email'],
                                             password=form.cleaned_data['password'])
        return  render(request, "user_profiles/login.html", {
    		"reg_form": form,
            "form":profile_forms.LoginForm
            })
