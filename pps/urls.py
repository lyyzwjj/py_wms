from django.urls import path
from pps import views

# 应用中url配置严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    path('index', views.index),
    path('filter', views.filter),
    path('create', views.create),
    path('delete/<int:did>', views.delete),
    path('menus', views.system_menu),
    path('temp_inherit', views.temp_inherit),
    path('temp_escape', views.temp_escape)
]
