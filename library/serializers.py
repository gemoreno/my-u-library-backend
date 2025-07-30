from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    available = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'year_published', 'stock', 'available']