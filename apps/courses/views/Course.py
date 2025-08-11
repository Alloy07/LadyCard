from rest_framework import generics
from models import Course
from serializers import (
    CourseListSerializer,
    CourseRetrieveSerializer,
    CourseCreateSerializer,
    CourseUpdateSerializer,
)


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializer


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseUpdateSerializer


class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
