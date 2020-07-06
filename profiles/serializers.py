from rest_framework import serializers

from .models import UserProfile


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


# class UpdateProfileSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
