from rest_framework import serializers

from profiles.models import UserProfile
from .models import Advert, Review


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
    """Get UserProfile object for each Advert and extract fields"""
    def to_representation(self, value):
        profile = UserProfile.objects.get(pk=value.pk)
        context = {
            'nickname': profile.nickname,
            'contact_link': profile.contact_link
        }
        return context

    class Meta:
        model = UserProfile
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    """Advert list"""
    user = AdvertOwnerSerializer(read_only=True)

    class Meta:
        model = Advert
        fields = ('id', 'user', 'title', 'price', 'published')


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


class AdvertCreateSerializer(serializers.ModelSerializer):
    """Create Advert object"""
    class Meta:
        model = Advert
        exclude = ['user']
