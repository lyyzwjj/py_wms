from django.urls import path
from learn_test import views

# 应用中url配置严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    path('index', views.index),
    path('login', views.login),
    path('login_check', views.login_check),
    path('ajax_test', views.ajax_test),
    path('ajax_handle', views.ajax_handle),
    path('ajax_login', views.ajax_login),
    path('ajax_login_check', views.ajax_login_check)
]
