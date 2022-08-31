"""surfa_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from surfa import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static




urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts',include('accounts.urls',namespace='accounts')),
    path('accounts',include('django.contrib.auth.urls')),
    path('', views.HomePage.as_view(),name='home'),
    #path('dashboard/', include('dashboard.urls')),
    path('portfolio/', views.PortfolioView.as_view(),name='portfolio'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'), # Auth routes - login / register
    path('membership/', views.Membership.as_view(),name='membership'),
    path('portfolio/', views.PortfolioView.as_view(),name='portfolio'),
    path('contact1/', views.Contact1.as_view(),name='contact1'),
    path('about1/', views.About1.as_view(),name='about1'),
    path('about/', views.About2.as_view(),name='about2'),
    path('faq/', views.FaqView.as_view(),name='faq'),
    path('post_index/', views.PostList.as_view(), name='post_index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/', include('blog.urls'),name='blog'),
    path('dashboard/', views.dashboard_with_pivot, name='dashboard'),
    path('data', views.pivot_data, name='pivot_data'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns +=[
        path('__debug__/', include(debug_toolbar.urls))
    ]+urlpatterns