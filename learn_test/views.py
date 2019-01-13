from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, request as r


# Create your views here.
def index(request):
    # i = 1/0;
    learn()
    return render(request, 'learn_test/index.html')


def login(request):
    return render(request, 'learn_test/login.html')


def login_check(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(username + ':' + password)
    if username == 'wjj' and password == 'wzzst310':
        return redirect('/learn_test/index')
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
