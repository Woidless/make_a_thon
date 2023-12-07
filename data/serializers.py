from rest_framework import serializers
from .models import DataTruck


class DataTruckSerializers(serializers.ModelSerializer):
    class Meta:
        model = DataTruck
        fields = '__all__'