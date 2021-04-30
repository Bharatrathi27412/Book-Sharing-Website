"""onlinelibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from login.views import login_view,postlogin_view,logout_view, dashboard_view
from registration.views import signup_view, postsignup_view
from dashboard.views import search_view
#from dashboard.views import dashboard_view
from upload.views import upload_view,postupload_view
from booklist.views import englist_view,medlist_view,lawlist_view,ecolist_view,otherlist_view,codelist_view,alluploads_view

urlpatterns = [
    #path('home/',home_view,name='home_view'),
    path('',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('postsignup/',postsignup_view,name='post_signup'),
    path('postlogin/',postlogin_view,name='post_login'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('upload/',upload_view,name='upload'),
    path('postupload/',postupload_view,name='postupload'),
    path('englist/',englist_view,name="englist"),
    path('medlist/',medlist_view,name="medlist"),
    path('lawlist/',lawlist_view,name="lawlist"),
    path('ecolist/',ecolist_view,name="ecolist"),
    path('otherlist/',otherlist_view,name="otherlist"),
    path('codelist/',codelist_view,name="codelist"),
    path('logout/',logout_view,name='logout'),
    path('all/',alluploads_view,name='all'),
    path('admin/', admin.site.urls),
    path('search/',search_view,name='search'),
    # url(r'^search/',search_view,name='search'),


]
