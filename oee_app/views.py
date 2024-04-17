from django.shortcuts import render
from rest_framework import viewsets
from .models import Machines, ProductionLog
from .serializers import MachinesSerializer, ProductionLogSerializer
from django.db.models import Sum
from rest_framework.response import Response

# ViewSet for Machines
class MachinesViewSet(viewsets.ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MachinesSerializer

# ViewSet for ProductionLog
class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer

    # Calculate OEE
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Calculate OEE
        results = []
        for log in queryset:
            machine = log.machine
            logs = ProductionLog.objects.filter(machine=machine)
            available_time = 3 * 8 * 60  # 3 shifts, each 8 hours

            actual_output = logs.aggregate(Sum('duration'))['duration__sum']
            good_products = logs.count()  # Assuming good products are those that follow ideal cycle time
            total_products = len(logs)

            # Ideal cycle time (assumed 5 minutes or 0.083 hours)
            ideal_cycle_time = 0.083

            available_operating_time = total_products * ideal_cycle_time
            unplanned_downtime = available_time - available_operating_time

            # OEE calculations
            availability = ((available_time - unplanned_downtime) / available_time) * 100
            performance = (ideal_cycle_time * actual_output / available_operating_time) * 100
            quality = (good_products / total_products) * 100

            oee = availability * performance * quality / 10000

            results.append({
                'machine': machine.machine_name,
                'oee': oee,
                'availability': availability,
                'performance': performance,
                'quality': quality,
            })

        # Render the template with results
        return render(request, 'oee_app/oee_data.html', {'results': results})

# View for displaying the OEE data
def oee_data(request):
    production_logs = ProductionLog.objects.all()
    results = []
    
    # Calculate OEE for each machine
    for log in production_logs:
        machine = log.machine
        logs = ProductionLog.objects.filter(machine=machine)
        available_time = 3 * 8 * 60  # 3 shifts, each 8 hours

        actual_output = logs.aggregate(Sum('duration'))['duration__sum']
        good_products = logs.count()  # Assuming good products are those that follow ideal cycle time
        total_products = len(logs)

        # Ideal cycle time (assumed 5 minutes or 0.083 hours)
        ideal_cycle_time = 0.083

        available_operating_time = total_products * ideal_cycle_time
        unplanned_downtime = available_time - available_operating_time

        # OEE calculations
        availability = ((available_time - unplanned_downtime) / available_time) * 100
        performance = (ideal_cycle_time * actual_output / available_operating_time) * 100
        quality = (good_products / total_products) * 100

        oee = availability * performance * quality / 10000

        results.append({
            'machine': machine.machine_name,
            'oee': oee,
            'availability': availability,
            'performance': performance,
            'quality': quality,
        })
    
    return render(request, 'oee_app/oee_data.html', {'results': results})
