from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from missions.models import Missions
from missions.serializers import MissionsSerializer, MissionDetailSerializer


class MissionsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class MissionsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = MissionsSerializer
    pagination_class = MissionsPagination
    queryset = Missions.objects.all()

    def get_serializer_class(self):
        if self.action == "Retrieve":
            return MissionDetailSerializer
        return MissionsSerializer
