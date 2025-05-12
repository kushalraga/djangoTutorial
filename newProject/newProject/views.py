from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello - You are on the Home Page')
    return render(request, 'website/home.html')

def about(request):
    # return HttpResponse('Hello - You are on the About Page')
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse('Hello - You are on the Contact Page')
    return render(request, 'website/contact.html')
