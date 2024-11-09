from django.db import models
from django.contrib.auth.models import User

RATING = ((1, "⭐"), (2, "⭐⭐"), (3, "⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (5, "⭐⭐⭐⭐⭐"))

class BookReview(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING, default=None)
    your_review = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.book_title}'
