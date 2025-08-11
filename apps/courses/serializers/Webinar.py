from rest_framework import serializers
from models import Webinar


class WebinarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ["id", "title", "price", "datetime", "rating"]

class WebinarRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = "__all__"

class WebinarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = [
            "title", "description", "price", "card",
            "category", "author", "datetime", "rating"
        ]

class WebinarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = [
            "title", "description", "price", "card",
            "category", "author", "datetime", "rating"
        ]