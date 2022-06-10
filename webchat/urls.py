"""websitechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from webchats import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("login.html", views.login),
    path("signup.html", views.signup),
    path("check", views.ssbuit, name='check'),
    path("checklet", views.subindb, name="checklet"),
    path("signup1.html", views.signup),
    path("signup2.html", views.signup),
    path("checklogin", views.checklogin, name='checklogin'),
    path("chatpage.html",views.chatpage),
     path('chatpage2.html',views.chatpage2),
    path('checkchat',views.checkchat,name="checkchat"),
    path('chatsend',views.chatsend,name="chatsend"),
    path(r'^reloadss/(?P<userid>\d+)/$/(?P<recevier>\d+)/$',views.reloadss,name="reloadss"),
    path('loginss',views.loginss,name='loginss')


]
