from rest_framework import serializers
from models import Comment



class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "course", "webinar", "rating"]

class CommentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "course", "webinar", "text", "rating"]

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "course", "webinar", "text", "rating"]