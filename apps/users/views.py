from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from .serializers import UserSerializer
from .models import UserProfile


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()