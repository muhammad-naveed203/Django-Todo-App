from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]

    def create(self, validated_data):
        User.objects.create_user(**validated_data)
        return validated_data

