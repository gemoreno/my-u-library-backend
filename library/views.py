from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def filtered_books(request):
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    genre = request.GET.get('genre', '')

    books = Book.objects.all()

    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__icontains=author)
    if genre:
        books = books.filter(genre__icontains=genre)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
