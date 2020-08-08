from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """Serialize UserProfile model object"""
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'avatar', 'username', 'email',
            'nickname', 'first_name', 'last_name',
            'messenger', 'contact_phone', 'contact_link',
            'about'
        )


class CreateProfileSerializer(serializers.ModelSerializer):
    """All profile fields"""
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
