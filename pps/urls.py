from django.urls import path
from pps import views

# 应用中url配置严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    path('index', views.index),
    path('create', views.create),
    path('delete/<int:did>', views.delete)
]
