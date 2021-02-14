from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DriverSerializer
from .models import Car, Driver

# Create your views here.

# Non-RestFramework View
# def car_detail(request, pk):
#     owner_obj = Driver.objects.get(pk=pk)
#     car_objs = Car.objects.filter(owner_id=owner_obj.id)
#     context = {
#         "vehicles": car_objs,
#         "drivers": owner_obj,
#     }
    
#     return render(request, "car_detail.html", context)

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().order_by('name')
    serializer_class = DriverSerializer