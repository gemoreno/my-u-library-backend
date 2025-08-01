from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from library.permissions.roles import IsStudent
from ..models import Book, CheckoutRecord
from ..serializers import BookSerializer
from django.db.models import Count, Q, F, ExpressionWrapper, IntegerField

@api_view(['GET'])
@permission_classes([AllowAny])
def filtered_books(request):
    title = request.GET.get('title', '').strip()
    author = request.GET.get('author', '').strip()
    genre = request.GET.get('genre', '').strip()

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

@api_view(['POST'])
@permission_classes([IsStudent])
def checkout_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.stock <= 0:
        return Response({"error": "No copies available."}, status=400)
    
    CheckoutRecord.objects.create(student=request.user, book=book)
    return Response({"message": "Book checked out successfully."})
