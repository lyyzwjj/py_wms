from django.shortcuts import render


# Create your views here.
def index(request):
    # i = 1/0;
    return render(request, 'learn_test/index.html')
