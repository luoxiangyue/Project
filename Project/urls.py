"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from missions.views import MissionsViewSet
from projects.views import ProjectListViewSet
from users.views import UserViewSet

router = DefaultRouter()

router.register(r'projects', ProjectListViewSet, base_name="projects")

router.register(r'user', UserViewSet, base_name="user")

router.register(r'missions', MissionsViewSet, base_name="missions")

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
