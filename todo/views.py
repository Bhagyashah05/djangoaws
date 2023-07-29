from django.shortcuts import render
from rest_framework import viewsets
from .serializers import todoserializers
from .models import todo


class todoview(viewsets.ModelViewSet):
    serializer_class=todoserializers
    queryset=todo.objects.all()


