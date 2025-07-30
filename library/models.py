from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    year_published = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
                                
class CheckoutRecord(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="checkout_records")
    is_returned = models.BooleanField(default=False)
    date_out = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(null=True, blank=True)
    