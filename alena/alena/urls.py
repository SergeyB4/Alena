
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import VimosViewSet


from django.contrib import admin
from django.urls import path

v1_router = DefaultRouter()
v1_router.register('api', VimosViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(v1_router.urls))
]
