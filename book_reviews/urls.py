from django.urls import path
from book_reviews import views

urlpatterns = [
    path('book_reviews/', views.BookReviewList.as_view()),
    path('book_reviews/<int:pk>/', views.BookReviewDetail.as_view())
]