from django.views.generic import ListView
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from .serializers import SensorDetailSerializer, Measurement
from .models import Sensor
from rest_framework import status

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class CreateSensor(APIView):
    def post(self, request):
        sensor = serializer.save()
        serializer = SensorDetailSerializer(data=request.data)
        
        return Response(request.data, status=status.HTTP_201_CREATED)
    
class UpdateSensor(APIView):
    def patch(self, request, pk):
        sensor = Sensor.get_object_or_404(pk=pk)
        serializer = SensorDetailSerializer(instance=sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(request.data)


@api_view
def get(request):
    sensors = Sensor.objects.all()
    serializer = SensorDetailSerializer(data=request.data, many = True)
    return Response(serializer.data)







    







