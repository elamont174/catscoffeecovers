from django.db import models
from django.contrib.auth.models import User
from book_reviews.models import BookReview


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BookReview, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    your_comment = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.your_comment