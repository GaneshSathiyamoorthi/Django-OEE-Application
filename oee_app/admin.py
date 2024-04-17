from django.contrib import admin
from .models import Machines, ProductionLog

# Register the Machines model
admin.site.register(Machines)

# Register the ProductionLog model
admin.site.register(ProductionLog)
