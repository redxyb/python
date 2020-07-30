'''
@Author: xyb
@Date: 2020-07-25 11:39:50
@LastEditTime: 2020-07-25 17:08:51
'''
from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('kobe.html/', views.kobe, name='kobe_page'),
    path('login.html/', views.login_page, name='login_page')
]