from rest_framework import generics
from models import Lesson
from serializers import (
    LessonListSerializer,
    LessonRetrieveSerializer,
    LessonCreateSerializer,
    LessonUpdateSerializer,
)

class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonRetrieveSerializer

class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonUpdateSerializer

class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
