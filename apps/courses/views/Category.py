from rest_framework import generics
from models import Category
from serializers import (
    CategoryListSerializer,
    CategoryRetrieveSerializer,
    CategoryCreateSerializer,
    CategoryUpdateSerializer,
)

class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerializer

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
