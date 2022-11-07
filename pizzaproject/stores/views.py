from django.shortcuts import render

from .models import Pizzeria
from rest_framework import generics
from .serializers import PizzeriaListSerializer,PizzeriaDetailSerializer

# Create your views here.

class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

class PizzeriaDeleteAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()



