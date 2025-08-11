from rest_framework import serializers
from models import Course



class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "price", "rating"]

class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "title", "description", "price", "card",
            "category", "author", "rating"
        ]

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "title", "description", "price", "card",
            "category", "author", "rating"
        ]
