from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'index.html')


def yes(request):
    return render(request ,'yes.html')


def no (request):
    return render(request , 'no.html')