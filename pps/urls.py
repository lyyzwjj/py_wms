from django.urls import path, re_path
from pps import views

app_name = 'pps'
# 应用中url配置严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    # path('index', views.index),
    path('index3', views.index, name='index'),
    path('filter', views.filter),
    path('create', views.create),
    path('delete/<int:did>', views.delete),
    path('menus', views.system_menu),
    path('temp_inherit', views.temp_inherit),
    path('temp_escape', views.temp_escape),
    path('change_pwd', views.change_pwd),
    path('change_pwd_action', views.change_pwd_action),
    path('login', views.login),
    path('login_check', views.login_check),
    path('verify_code', views.verify_code),
    path('reverse_index', views.reverse_index),
    path('static_test', views.static_test),
    path('test_redirect', views.test_redirect),
    path('show_args/<int:a>/<int:b>', views.show_args, name='show_args'),
    re_path('show_kwargs/(?P<c>\d+)/(?P<d>\d+)', views.show_kwargs, name='show_kwargs'),

]
