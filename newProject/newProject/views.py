from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello - You are on the Home Page')

def about(request):
    return HttpResponse('Hello - You are on the About Page')

def contact(request):
    return HttpResponse('Hello - You are on the Contact Page')
