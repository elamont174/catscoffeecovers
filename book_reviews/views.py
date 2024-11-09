from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookReview
from .serializers import BookReviewSerializer

class BookReviewList(APIView):
    serializer_class = BookReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        book_reviews = BookReview.objects.all()
        serializer = BookReviewSerializer(
            book_reviews, many=True, context={'request': request}
        )
        return Response(serializer.data)

def book_review(self, request):
    serializer = BookReviewSerializer(
        data = request.data, context={'request': request}
    )
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )
