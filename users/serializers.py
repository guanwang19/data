from rest_framework import serializers
from .models import User  # Ensure this import is correct

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "display_name", "password"]

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        user = User.objects.create_user(**validated_data)
        return user
