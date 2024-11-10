from rest_framework import serializers
from .models import BookReview

class BookReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    id = serializers.ReadOnlyField(source='owner.profile.id')
    image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = BookReview
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'book_title',
            'author', 'genre', 'rating', 'your_review', 'image', 'is_owner',
        ]