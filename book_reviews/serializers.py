from rest_framework import serializers
from .models import BookReview
from likes.models import Like

class BookReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
            user = self.context['request'].user
            if user.is_authenticated:
                like = Like.objects.filter(
                    owner=user, post=obj
                ).first()
                return like.id if like else None
            return None

    class Meta:
        model = BookReview
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'created_at', 'updated_at', 
            'book_title', 'author', 'genre', 'rating', 'your_review', 'image', 
            'like_id', 'likes_count', 'comments_count',
        ]