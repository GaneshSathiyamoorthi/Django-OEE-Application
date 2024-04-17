from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router instance
router = DefaultRouter()

# Register the viewsets for the API
router.register(r'machines', views.MachinesViewSet)
router.register(r'production_logs', views.ProductionLogViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the API router URLs under the 'api/' path
    path('api/', include(router.urls)),
    
    # Define the frontend URL for displaying OEE data
    path('', views.oee_data, name='oee_data'),
]
