from django.shortcuts import render
from api.models import Vimos
from rest_framework import viewsets
from api.serializers import VimosSerializer


class VimosViewSet(viewsets.ModelViewSet):
    """Вьюсет для управления пользователями."""
    queryset = Vimos.objects.all()
    serializer_class = VimosSerializer