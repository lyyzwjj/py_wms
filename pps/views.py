from django.shortcuts import render, redirect
from pps.models import Department
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
