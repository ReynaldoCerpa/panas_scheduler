# from django.http import HttpResponse 
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello World! Im Home.')
    return render(request, 'home.html')
	
def about(request):
    # return HttpResponse('My About page.')
    return render(request, 'about.html')

def users(request):
    return render(request, 'users.html')
