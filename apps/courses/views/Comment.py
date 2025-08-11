from rest_framework import generics
from models import Comment
from serializers import (
    CommentListSerializer,
    CommentRetrieveSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
)

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

class CommentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveSerializer

class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer

class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
