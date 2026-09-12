from django.urls import path
from .views import CreateSensor, UpdateSensor, get


urlpatterns = [
    '/new/', CreateSensor.as_view(),
    '/set/', UpdateSensor.as_view(),
    '/all/', get
]
