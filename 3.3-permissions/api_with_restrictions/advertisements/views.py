from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements import filters
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()          
    serializer_class = AdvertisementSerializer     
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = filters.AdvertisementFilter
    filterset_fields = ['status', 'creator']       
    search_fields = ['title', 'description']        
    ordering_fields = ['created_at', 'updated_at']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
