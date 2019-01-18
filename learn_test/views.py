from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, request as r
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    # i = 1/0;
    learn()
    return render(request, 'learn_test/index.html')


def login(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'learn_test/login.html', {'username': username})


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
        response = redirect('/learn_test/index')
        if remember == 'on':
            response.set_cookie('username', username, max_age=10 * 24 * 3600)
        return response
    else:
        return redirect('/learn_test/login')
    return HttpResponse('OK')


def learn():
    q = r.QueryDict("a=18&a='66'&b='4'")
    print(q['a'])
    print(q.get('b'))


def ajax_test(request):
    return render(request, 'learn_test/ajax_test.html')


def ajax_handle(request):
    return JsonResponse({"res": 1})


def ajax_login(request):
    return render(request, 'learn_test/login_ajax.html')


def ajax_login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'wjj' and password == 'wzzst310':
        return JsonResponse({"res": 1})
    else:
        return JsonResponse({"res": 0})


def set_cookie(request):
    response = HttpResponse('设置cookie')
    # response.set_cookie('num', 1)
    # 设置两周之后过期
    response.set_cookie('num', 1, expires=datetime.now() + timedelta(days=14))
    # response.set_cookie('num', 1, max_age=10)# max_age 单位s
    # response.set_cookie('num', 1, max_age=14*24*3600)# max_age 单位s
    # response.set_cookie('num', 1)
    return response


def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)


def set_session(request):
    request.session['username'] = 'smart'
    request.session['age'] = 18
    # response.set_cookie('num', 1)
    # del request.session['age']删除session
    # request.session.set_expiry(1 * 24 * 3600) 设置过期时间
    return HttpResponse('设置session')


def get_session(request):
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ":" + str(age))


def clear_session(request):
    request.session.clear()
    return HttpResponse('清除成功')


def flush_session(request):
    request.session.flush()
    return HttpResponse('删除成功')


