from rest_framework import serializers
from .models import Pizzeria

class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'logo_image',
            'city',
            'zipcode',
        ]
        
        
class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'street',
            'city',
            'state', 
            'zipcode',
            'website',
            'phone_number', 
            'description', 
            'logo_image',
            'email',
            'active',
        ]

