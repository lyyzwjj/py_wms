from django.shortcuts import render, redirect
from pps.models import Department, SystemMenu, NewsInfo
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    departments = Department.objects.all()
    return render(request, 'pps/index.html', {'departments': departments})


def filter(request):
    news = NewsInfo.objects.all()
    return render(request, 'pps/filter.html', {'news': news})


def create(request):
    d = Department()
    d.name = '综管部'
    d.sn = 'Comprehensive Department'
    d.save()
    # return HttpResponse('OK')
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request, did):
    d = Department.objects.get(id=did)
    d.delete()
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def system_menu(request):
    menu = SystemMenu.objects.get(name='角色管理')
    menu_parent = menu.parent
    menu_children = menu.systemmenu_set.all()
    return render(request, 'pps/menus.html', {'menu': menu, 'parent': menu_parent, 'children': menu_children})


def temp_inherit(request):
    return render(request, 'pps/child.html')


def temp_escape(request):
    return render(request, 'pps/html_escape.html', {'content': '<h1>hello</h1>'})


def login(request):
    if request.session['islogin']:
        return redirect('pps/change_pwd')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'pps/login.html', {'username': username})


def login_check(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    # remember = request.POST['remember']
    # cookie 只能get出来 不在QueryDict里面
    remember = request.POST.get('remember')
    print(remember)
    print(username + ':' + password)
    if username == 'wjj' and password == 'wzzst310':
        response = redirect('/pps/change_pwd')
        if remember == 'on':
            response.set_cookie('username', username, max_age=10 * 24 * 3600)
        request.session['islogin'] = True
        request.session['username'] = username
        return response
    else:
        return redirect('/pps/login')
    return HttpResponse('OK')


def login_required(view_func):
    '''登录判断装饰器'''

    def wrapper(request, *view_args, **view_kwargs):
        if request.session['islogin']:
            return view_func(request, *view_args, **view_kwargs)
        else:
            return redirect('/pps/login')

    return wrapper


@login_required
def change_pwd(request):
    #    if not request.session.has_key('islogin'):
    #        return redirect('/pps/login')
    return render(request, 'pps/change_pwd.html')


@login_required
def change_pwd_action(request):
    pwd = request.POST['pwd']
    username = request.session['username']
    return HttpResponse('%s修改密码为:%s' % (username, pwd))
