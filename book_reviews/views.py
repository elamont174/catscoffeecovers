from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookReview
from .serializers import BookReviewSerializer
from catscoffeecovers.permissions import IsOwnerOrReadOnly

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

    def post(self, request):
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

class BookReviewDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookReviewSerializer

    def get_object(self,pk):
        try:
            post = BookReview.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except BookReview.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = BookReviewSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = BookReviewSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
       post = self.get_object(pk)
       post.delete()
       return Response(
        status=status.HTTP_204_NO_CONTENT
       )
