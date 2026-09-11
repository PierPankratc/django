from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=150, null=True)

class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    t = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, name='measurements')

