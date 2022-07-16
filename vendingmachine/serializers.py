from rest_framework import serializers
from .models import vending_machine
class itemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = vending_machine
        fields = ['id', 'itemName', 'itemPrice', 'itemInStock', 'image']

    
