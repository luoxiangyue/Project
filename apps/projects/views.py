from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import ProjectsSerializer
from .serializers import Projects


class ProjectsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ProjectListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):

    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()