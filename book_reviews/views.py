from rest_framework import generics, permissions
from catscoffeecovers.permissions import IsOwnerOrReadOnly
from .models import BookReview
from .serializers import BookReviewSerializer


class BookReviewList(generics.ListCreateAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BookReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = BookReview.objects.all()