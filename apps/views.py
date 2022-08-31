from django.views.generic import (View,TemplateView,ListView)
from django.views import generic
from django.views import generic
from blog.models import Post
from django.shortcuts import render
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers
# Create your views here.

class HomePage(TemplateView):
    template_name = 'surfa/index.html'


class Membership(TemplateView):
    template_name = 'surfa/membership.html'

class Base2(TemplateView):
    template_name = 'surfa/base2.html'


class PortfolioView(TemplateView):
    template_name = 'surfa/portfolio.html'

class Contact1(TemplateView):
    template_name = 'surfa/contact-1.html'

class About1(TemplateView):
    template_name = 'surfa/about-1.html'

class About2(TemplateView):
    template_name = 'surfa/about-2'

class FaqView(TemplateView):
    template_name = 'surfa/faq-1.html'

