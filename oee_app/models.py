from django.db import models

class Machines(models.Model):
    machine_name = models.CharField(max_length=255)
    machine_serial_no = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

class ProductionLog(models.Model):
    cycle_no = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=255, unique=True)
    material_name = models.CharField(max_length=255)
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()  # Duration in hours

    def __str__(self):
        return self.unique_id
