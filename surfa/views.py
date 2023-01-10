
from django.views.generic import (View,TemplateView,ListView)
from django.views import generic
from django.views import generic
from .models import Post_Projects
from blog.models import Post
from django.shortcuts import render
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Order
from django.core import serializers
# Create your views here.

class HomePage(TemplateView):
    template_name = 'surfa/index2.html'


class Membership(TemplateView):
    template_name = 'surfa/membership.html'

class Base2(TemplateView):
    template_name = 'surfa/base2.html'


#class PortfolioView(TemplateView):
#    template_name = 'surfa/portfolio.html'

class PortfolioView(generic.ListView):
    queryset = Post_Projects.objects.filter(status=1)
    template_name = 'surfa/portfolio.html'

class Contact1(TemplateView):
    template_name = 'surfa/contact-1.html'

class About1(TemplateView):
    template_name = 'surfa/about-1.html'

class About2(TemplateView):
    template_name = 'surfa/about-2'

class FaqView(TemplateView):
    template_name = 'surfa/faq-1.html'


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def dashboard_with_pivot(request):
    return render(request, 'dashboard/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)