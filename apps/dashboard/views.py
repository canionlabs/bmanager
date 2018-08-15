from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name='home.html'