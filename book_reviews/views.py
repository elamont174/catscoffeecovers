from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from catscoffeecovers.permissions import IsOwnerOrReadOnly
from .models import BookReview
from .serializers import BookReviewSerializer


class BookReviewList(generics.ListCreateAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BookReview.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'book_title',
        'author',
        'genre',
    ]
    ordering_fields = [
        'likes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = BookReview.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')
