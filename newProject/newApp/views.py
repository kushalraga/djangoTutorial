from django.shortcuts import render
from .models import TeamMembers

# Create your views here.
def newapp(request):
    team_members = TeamMembers.objects.all()
    return render(request, 'newApp/newapp.html', {'team_members' : team_members})