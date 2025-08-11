from rest_framework import generics
from models import Module
from serializers import (
    ModuleListSerializer,
    ModuleRetrieveSerializer,
    ModuleCreateSerializer,
    ModuleUpdateSerializer,
)

class ModuleCreateAPIView(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleCreateSerializer

class ModuleListAPIView(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleListSerializer

class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleRetrieveSerializer

class ModuleUpdateAPIView(generics.UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleUpdateSerializer

class ModuleDeleteAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
