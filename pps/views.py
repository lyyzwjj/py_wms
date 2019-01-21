from django.shortcuts import render, redirect
from pps.models import Department, SystemMenu, NewsInfo
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from django.conf import settings


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
    if request.session.get('islogin'):
        return redirect('/pps/change_pwd')
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
    vcode = request.POST.get('vcode')
    verifycode = request.session.get('verifycode')
    if vcode != verifycode:
        return redirect('/pps/login')
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


def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # mac font = ImageFont.truetype('Arial.ttf', 23)
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    # import io
    # buf = io.BytesIO()
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def reverse_index(request):
    return render(request, 'pps/reverse_index.html')


def show_args(request, a, b):
    return HttpResponse(str(a) + ':' + str(b))


def show_kwargs(request, c, d):
    return HttpResponse(str(c) + ':' + str(d))


from django.urls import reverse


def test_redirect(request):
    # url = reverse('pps:index')
    # url = reverse('pps:show_args', args=(1, 2))
    # url = reverse('pps:show_args', args={'a': 3, 'b': 4}) 这样写不行
    url = reverse('pps:show_kwargs', kwargs={'c': 3, 'd': 4})
    return redirect(url)


def static_test(request):
    # ['/Users/wjj/PycharmProjects/wms/static']
    # ['/home/wjj/PycharmProjects/wms/static']
    settings
    print(type(settings))
    print(settings.STATICFILES_DIRS)
    print(settings.STATICFILES_FINDERS)
    # ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
    return render(request, 'pps/static_test.html')
