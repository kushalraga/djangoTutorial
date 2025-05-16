from django.shortcuts import render, get_object_or_404
from .models import Services

# Create your views here.
def all_services(request):
    services = Services.objects.all()
    return render(request, 'services/all_services.html', {'services' : services})

def service_details(request, service_id):
    service = get_object_or_404(Services, id = service_id)
    context = {
        'service': service,
    }
    return render(request, 'services/single_service.html', context)