from django.shortcuts import render, redirect
from pps.models import Department, SystemMenu
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    departments = Department.objects.all()
    return render(request, 'pps/index.html', {'departments': departments})


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
