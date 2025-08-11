from rest_framework import generics
from models import Webinar
from serializers import (
    WebinarListSerializer,
    WebinarRetrieveSerializer,
    WebinarCreateSerializer,
    WebinarUpdateSerializer,
)

class WebinarCreateAPIView(generics.CreateAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarCreateSerializer

class WebinarListAPIView(generics.ListAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarListSerializer

class WebinarRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarRetrieveSerializer

class WebinarUpdateAPIView(generics.UpdateAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarUpdateSerializer

class WebinarDeleteAPIView(generics.DestroyAPIView):
    queryset = Webinar.objects.all()
