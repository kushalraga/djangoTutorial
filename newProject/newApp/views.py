from django.shortcuts import render

# Create your views here.
def newapp(request):
    return render(request, 'newApp/newapp.html')