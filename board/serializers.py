from rest_framework import serializers

from .models import Advert, Review


class FilterReviewSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)

        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Find all children in recursive way"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)

        return serializer.data


class AdvertSerializer(serializers.ModelSerializer):
    """Advert list"""

    class Meta:
        model = Advert
        fields = ('id', 'user', 'title', 'published')


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
