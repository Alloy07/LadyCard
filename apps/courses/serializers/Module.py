from rest_framework import serializers
from models import Module

class ModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["id", "name", "course"]

class ModuleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"

class ModuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["course", "name", "icon"]

class ModuleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["course", "name", "icon"]
