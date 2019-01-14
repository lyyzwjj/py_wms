from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse


def my_render(request, template_path, context={}):
    # 1 加载模板文件,获取一个模板对象
    temp = loader.get_template(template_path)
    # 2 定义模板上下文,给模板文件传递数据
    # context = RequestContext(request, context)
    # 3 模板渲染,产生一个替换后的html内容
    res_html = temp.render(context)
    # 4 返回应答
    return HttpResponse(res_html)


# Create your views here.
def index(request):
    # return my_render(request, 'app/index.html')
    return render(request, 'app/index.html')


def index2(request):
    # return my_render(request, 'app/index.html')
    return render(request, 'app/index2.html')
