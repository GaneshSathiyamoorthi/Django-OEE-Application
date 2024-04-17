from rest_framework import serializers
from .models import Machines, ProductionLog

class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = '__all__'

class ProductionLogSerializer(serializers.ModelSerializer):
    machine = MachinesSerializer()

    class Meta:
        model = ProductionLog
        fields = '__all__'
