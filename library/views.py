from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.db.models import Count, Q, F, ExpressionWrapper, IntegerField

@api_view(['GET'])
def filtered_books(request):
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    genre = request.GET.get('genre', '')

    books = Book.objects.filter(
        title__icontains=title,
        author__icontains=author,
        genre__icontains=genre
    ).annotate(
        available=ExpressionWrapper(
            F('stock') - Count('checkout_records', filter=Q(checkout_records__is_returned=False)),
            output_field=IntegerField()
        )
    )

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
