from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import LoginForm

class login(LoginView):
    form_class = LoginForm
    template_name = 'register/login.html'

class Logout(LogoutView):
    template_name = 'register/login.html'

# Create your views here.
