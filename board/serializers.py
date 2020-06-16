from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Advert, Review
from profiles.models import UserProfile


class FilterReviewSerializer(serializers.ListSerializer):
    """Filter primary review with parent=null"""
    def to_representation(self, data):
        data = data.filter(parent=None)

        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Find all children in recursive way"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)

        return serializer.data


class AdvertOwnerSerializer(serializers.ModelSerializer):
    """Serialize some User fields for list of adverts"""

    class Meta:
        model = User
        fields = ('nickname', 'contact_link')


class AdvertSerializer(serializers.ModelSerializer):
    """Advert list"""
    owner = AdvertOwnerSerializer(read_only=True)

    class Meta:
        model = Advert
        fields = ('id', 'owner', 'title', 'published')


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Review object create serializer"""

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Review object serializer"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = ('id', 'user', 'text', 'published', 'children')


class AdvertDetailSerializer(serializers.ModelSerializer):
    """Advert detail"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    platform = serializers.SlugRelatedField(slug_field='name', read_only=True)
    advert_category = serializers.SlugRelatedField(
        slug_field='name', read_only=True
    )
    content_type = serializers.SlugRelatedField(
        slug_field='name', read_only=True
    )
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Advert
        fields = '__all__'
