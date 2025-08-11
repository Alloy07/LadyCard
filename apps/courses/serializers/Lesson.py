from rest_framework import serializers
from models import Lesson



class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "module", "duration"]

class LessonRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["module", "title", "description", "file", "duration"]

class LessonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["module", "title", "description", "file", "duration"]

