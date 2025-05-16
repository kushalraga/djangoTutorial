# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.all_services, name='services'),
    path('<int:service_id>/', views.service_details, name='single_service'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact')
]
